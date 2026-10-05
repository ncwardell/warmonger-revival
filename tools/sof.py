#!/usr/bin/env python3
"""Decrypt/encrypt the client's .sof config files.

The client's CEncDecrypt uses Windows CryptoAPI (Base Provider defaults):
RC4 with a 40-bit key derived from MD5("CEncDecrypt Default Password"), i.e.
the first 5 hash bytes followed by 11 zero salt bytes. Plaintext is a
UTF-16LE INI with BOM.

  sof.py decrypt serverlist.sof > serverlist.ini
  sof.py encrypt serverlist.ini > serverlist.sof
  sof.py point serverlist.sof <host>   # rewrite in place: Login/gs1 -> host, web -> host:8080
"""
import hashlib
import re
import sys

KEY = hashlib.md5(b"CEncDecrypt Default Password").digest()[:5] + bytes(11)


def rc4(key, data):
    s = list(range(256))
    j = 0
    for i in range(256):
        j = (j + s[i] + key[i % len(key)]) & 255
        s[i], s[j] = s[j], s[i]
    i = j = 0
    out = bytearray()
    for c in data:
        i = (i + 1) & 255
        j = (j + s[i]) & 255
        s[i], s[j] = s[j], s[i]
        out.append(c ^ s[(s[i] + s[j]) & 255])
    return bytes(out)


def point(path, host):
    """Rewrite a serverlist.sof so the client talks to `host` (ports kept, web moved to 8080)."""
    text = rc4(KEY, open(path, "rb").read()).decode("utf-16")
    text = re.sub(r"^(Login|gs\d+)(\s*=\s*)[^:\r\n]+:", lambda m: f"{m[1]}{m[2]}{host}:", text, flags=re.M)
    text = re.sub(r"^(web\s*=\s*)[^\r\n]*", lambda m: f"{m[1]}{host}:8080", text, flags=re.M)
    with open(path, "wb") as f:
        f.write(rc4(KEY, b"\xff\xfe" + text.encode("utf-16-le")))
    print("".join(line for line in text.splitlines(True) if re.match(r"(Login|gs\d+|web)\s*=", line)), end="")


def main():
    mode, path = sys.argv[1], sys.argv[2]
    if mode == "point":
        return point(path, sys.argv[3])
    data = open(path, "rb").read()
    if mode == "decrypt":
        sys.stdout.write(rc4(KEY, data).decode("utf-16"))
    elif mode == "encrypt":
        text = data.decode("utf-8")
        sys.stdout.buffer.write(rc4(KEY, b"\xff\xfe" + text.encode("utf-16-le")))
    else:
        sys.exit(__doc__)


if __name__ == "__main__":
    main()
