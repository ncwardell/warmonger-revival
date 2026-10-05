#!/usr/bin/env python3
"""Python test server: login 8815, game 8813, web 8080; one shared world timer."""
import asyncio
import importlib
import pathlib
import struct
import sys
from urllib.parse import parse_qsl

import handlers
import sessions
from proto import deobfuscate, split

TICK_SECONDS = 0.2
WATCHED = (handlers.skills, handlers.loot, handlers.units, handlers.ai, handlers.quests, handlers)
_mtimes = {m.__name__: pathlib.Path(m.__file__).stat().st_mtime_ns for m in WATCHED}


def current():
    """Reload packet code on save; connection and world state remain alive."""
    global _mtimes
    changed = {m.__name__: pathlib.Path(m.__file__).stat().st_mtime_ns for m in WATCHED}
    if changed != _mtimes:
        _mtimes = changed
        snapshots = {m: m.__dict__.copy() for m in WATCHED}
        try:
            # Reject syntax errors before executing any of the changed modules.
            for module in WATCHED:
                path = pathlib.Path(module.__file__)
                compile(path.read_bytes(), str(path), "exec")
            importlib.invalidate_caches()
            importlib.reload(handlers)
            handlers.log("reloaded packet code; sessions preserved")
        except Exception as e:
            for module, namespace in snapshots.items():
                module.__dict__.clear()
                module.__dict__.update(namespace)
            handlers.log(f"reload failed, retaining previous code: {e!r}")
    return handlers


def send(writer, data):
    if not data or writer.is_closing():
        return
    try:
        writer.write(data)
        if writer.transport.get_write_buffer_size() > 1024 * 1024:
            writer.close()  # stop a stalled test client from buffering forever
    except (ConnectionError, OSError):
        writer.close()


async def ticker():
    """One timer for the whole world, independent of the connection count."""
    while True:
        await asyncio.sleep(TICK_SECONDS)
        try:
            current().tick()
        except Exception as e:
            handlers.log(f"[world] tick failed: {e!r}")


def handler(name, table, ticks=False):
    async def handle(reader, writer):
        peer = writer.get_extra_info("peername")
        session = None
        handlers.log(f"[{name}] connect {peer}")
        try:
            if ticks:
                session = sessions.connect(lambda data: send(writer, data))
            buffer = b""
            while data := await reader.read(65536):
                packets, buffer = split(buffer + data)
                for packet in packets:
                    opcode, extra, tick, key, body = deobfuscate(packet)
                    # Keep protocol evidence, but omit login tokens and tickets.
                    detail = "<login redacted>" if opcode in (0x4200, 0x4207) else body.hex()
                    handlers.log(f"[{name}] <- op=0x{opcode:04x} extra=0x{extra:04x} key=0x{key:04x} len={len(packet)} body={detail}")
                    out = current().dispatch(table, packet[:16] + body, session)
                    if out:
                        replies, rest = split(out)
                        if rest:
                            raise ValueError("handler returned an incomplete packet")
                        handlers.log(f"[{name}] -> " + ", ".join(
                            f"op=0x{struct.unpack_from('<H', p, 4)[0]:04x} len={len(p)}" for p in replies))
                        send(writer, out)
                    await writer.drain()
        except (ValueError, struct.error, ConnectionError, OSError) as e:
            handlers.log(f"[{name}] closing {peer}: {e}")
        except Exception as e:
            handlers.log(f"[{name}] connection failed: {e!r}")
        finally:
            if session is not None:
                try:
                    current().disconnect(session)
                except Exception as e:
                    handlers.log(f"[{name}] disconnect/save failed: {e!r}")
            writer.close()
            try:
                await writer.wait_closed()
            except (ConnectionError, OSError):
                pass
            handlers.log(f"[{name}] disconnect {peer}")
    return handle


async def handle_http(reader, writer):
    """Read a complete form POST, even when TCP splits its headers and body."""
    try:
        head = await asyncio.wait_for(reader.readuntil(b"\r\n\r\n"), timeout=10)
        headers = dict(line.split(b":", 1) for line in head.split(b"\r\n")[1:] if b":" in line)
        length = next((int(v) for k, v in headers.items() if k.lower() == b"content-length"), 0)
        if not 0 <= length <= 65536:
            raise ValueError("HTTP body is too large")
        body = await asyncio.wait_for(reader.readexactly(length), timeout=10)
        path = head.split(b" ")[1].decode() if b" " in head else ""
        form = dict(parse_qsl(body.decode(errors="replace")))
        page = current().WEB_PAGES.get(path)
        content = page(form).encode() if page else b""
        handlers.log(f"[web] <- {path} -> {len(content)} bytes")
        send(writer, b"HTTP/1.1 200 OK\r\nContent-Type: application/json\r\nConnection: close\r\n"
             + f"Content-Length: {len(content)}\r\n\r\n".encode() + content)
        await writer.drain()
    except (asyncio.TimeoutError, ConnectionError, OSError, ValueError,
            asyncio.IncompleteReadError, asyncio.LimitOverrunError):
        pass
    finally:
        writer.close()
        try:
            await writer.wait_closed()
        except (ConnectionError, OSError):
            pass


async def main(host="127.0.0.1"):
    servers = []
    ticking = None
    try:
        servers.append(await asyncio.start_server(handler("login", "LOGIN_REPLIES"), host, 8815))
        servers.append(await asyncio.start_server(handler("game", "GAME_REPLIES", ticks=True), host, 8813))
        servers.append(await asyncio.start_server(handle_http, host, 8080))
        ticking = asyncio.create_task(ticker())
        handlers.log(f"listening on {host}:8815 (login), {host}:8813 (game), {host}:8080 (web)")
        await asyncio.gather(*(s.serve_forever() for s in servers))
    finally:
        if ticking:
            ticking.cancel()
            await asyncio.gather(ticking, return_exceptions=True)
        for server in servers:
            server.close()
            await server.wait_closed()


if __name__ == "__main__":
    try:
        asyncio.run(main(sys.argv[1] if len(sys.argv) > 1 else "127.0.0.1"))
    except KeyboardInterrupt:
        pass
