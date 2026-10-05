#!/usr/bin/env python3
"""Stub login (8815), game (8813) and web (8080) servers for the Warmonger client.

Logs every packet the client sends. Replies come from handlers.py, which is
reloaded on change so the client can stay connected while handlers are edited.
"""
import asyncio
import importlib
import pathlib
import struct
import sys

import handlers
from proto import deobfuscate, split

HOST = sys.argv[1] if len(sys.argv) > 1 else "127.0.0.1"
# How often handlers.tick() runs per game connection (monster AI, respawns).
TICK_SECONDS = 0.2
HANDLERS_FILE = pathlib.Path(handlers.__file__)
_mtime = HANDLERS_FILE.stat().st_mtime


def current():
    """handlers, reloaded if the file changed since last use."""
    global _mtime
    mtime = HANDLERS_FILE.stat().st_mtime
    if mtime != _mtime:
        _mtime = mtime
        try:
            importlib.reload(handlers)
            handlers.log("reloaded handlers.py")
        except Exception as e:
            handlers.log(f"handlers.py reload failed, keeping old version: {e!r}")
    return handlers


def opcode_of(packet):
    return struct.unpack_from("<H", packet, 4)[0]


def handler(name, table, ticks=False):
    async def ticker(writer):
        """Send whatever handlers.tick() produces, every TICK_SECONDS, while connected."""
        while not writer.is_closing():
            await asyncio.sleep(TICK_SECONDS)
            tick = getattr(current(), "tick", None)
            try:
                out = tick() if tick else None
            except Exception as e:
                handlers.log(f"[{name}] tick failed: {e!r}")
                continue
            if out:
                writer.write(out)
                await writer.drain()

    async def handle(reader, writer):
        peer = writer.get_extra_info("peername")
        handlers.log(f"[{name}] connect {peer}")
        ticking = asyncio.create_task(ticker(writer)) if ticks else None
        buffer = b""
        while data := await reader.read(65536):
            buffer += data
            try:
                packets, buffer = split(buffer)
            except ValueError as e:
                handlers.log(f"[{name}] {e}; raw {data.hex()}")
                buffer = b""
                continue
            for p in packets:
                opcode, extra, tick, key, body = deobfuscate(p)
                handlers.log(f"[{name}] <- op=0x{opcode:04x} extra=0x{extra:04x} key=0x{key:04x} len={len(p)} body={body.hex()}")
                if reply := getattr(current(), table).get(opcode):
                    try:
                        # Handlers see the deobfuscated packet: header + plain payload.
                        out = reply(p[:16] + body)
                    except Exception as e:
                        handlers.log(f"[{name}] handler for 0x{opcode:04x} failed: {e!r}")
                        continue
                    if not out:
                        continue
                    replies, _ = split(out)
                    handlers.log(f"[{name}] -> " + ", ".join(f"op=0x{opcode_of(r):04x} len={len(r)}" for r in replies))
                    writer.write(out)
                    await writer.drain()
        handlers.log(f"[{name}] disconnect {peer}")
        if ticking:
            ticking.cancel()
        writer.close()
    return handle


async def handle_http(reader, writer):
    """The `web` endpoint from serverlist.sof (ASP pages returning XML)."""
    request = await reader.read(65536)
    head, _, body = request.partition(b"\r\n\r\n")
    path = head.split(b" ")[1].decode() if b" " in head else ""
    form = dict(pair.split("=", 1) for pair in body.decode(errors="replace").split("&") if "=" in pair)
    page = current().WEB_PAGES.get(path)
    content = page(form).encode() if page else b""
    handlers.log(f"[web] <- {path} {form} -> {len(content)} bytes{'' if page else ' (unhandled)'}")
    writer.write(
        b"HTTP/1.1 200 OK\r\nContent-Type: text/xml\r\nConnection: close\r\n"
        + f"Content-Length: {len(content)}\r\n\r\n".encode()
        + content
    )
    await writer.drain()
    writer.close()


async def main():
    servers = [
        await asyncio.start_server(handler("login", "LOGIN_REPLIES"), HOST, 8815),
        await asyncio.start_server(handler("game", "GAME_REPLIES", ticks=True), HOST, 8813),
        await asyncio.start_server(handle_http, HOST, 8080),
    ]
    handlers.log(f"listening on {HOST}:8815 (login), {HOST}:8813 (game), {HOST}:8080 (web)")
    await asyncio.gather(*(s.serve_forever() for s in servers))


asyncio.run(main())
