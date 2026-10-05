#!/usr/bin/env python3
"""Render contract/*.yaml into wiki pages under docs/contract/.

The YAML files are the source of truth (the server reads them, PRs edit them);
the pages are generated so the wiki always matches. Run from the repo root:
  python3 wiki/contract_pages.py contract docs/contract
Needs PyYAML.
"""
import pathlib
import sys

import yaml

TITLES = {
    "session": "Session: login, characters, channels",
    "world": "World: entry, warps, units, movement",
    "combat": "Combat: attacks, skills, damage, death",
    "items": "Items: inventory, equipment, shops, crafting",
    "quests": "Quests, NPCs and achievements",
    "social": "Social: chat, party, guild, friends, mail",
    "pvp": "PvP: matches, rooms, forts, wars",
    "system": "System: messages, GM, misc",
}


def hexop(value):
    return f"0x{value:x}" if isinstance(value, int) else str(value)


def cell(value):
    """A value safe inside a Markdown table cell."""
    if value is None:
        return ""
    text = hexop(value) if isinstance(value, int) and not isinstance(value, bool) else str(value)
    return text.replace("|", "\\|").replace("\n", " ")


def header_comment(path):
    """The YAML file's leading # comment block, as plain text."""
    lines = []
    for line in path.read_text().splitlines():
        if not line.startswith("#"):
            break
        lines.append(line[1:].removeprefix(" "))
    return "\n".join(lines).strip()


def fields_table(fields):
    rows = ["| Offset | Type | Field | Values | Notes |", "|---|---|---|---|---|"]
    for f in fields or []:
        if isinstance(f, dict):
            rows.append(
                f"| {cell(f.get('offset'))} | {cell(f.get('type'))} | {cell(f.get('name'))} "
                f"| {cell(f.get('values'))} | {cell(f.get('notes'))} |"
            )
    return "\n".join(rows)


def direction_block(label, spec):
    if not isinstance(spec, dict):
        return [f"**{label}:** {spec}", ""] if spec else []
    out = [f"**{label}**"]
    size = spec.get("size", spec.get("min_size"))
    facts = []
    if size is not None:
        facts.append(f"{'size' if 'size' in spec else 'min size'} {cell(size)}")
    if spec.get("extra"):
        facts.append(f"extra: {cell(spec['extra'])}")
    if facts:
        out.append("— " + "; ".join(facts))
    out.append("")
    if spec.get("fields"):
        out += [fields_table(spec["fields"]), ""]
    if spec.get("accepted_if"):
        out += [f"Accepted if: {spec['accepted_if']}", ""]
    return out


def opcode_section(op):
    tags = [op.get("direction", ""), f"confidence {op.get('confidence', '?')}"]
    if op.get("verified"):
        tags.append("verified")
    out = [f"### {hexop(op.get('opcode'))} {op.get('name', '')}", "", "*" + " · ".join(t for t in tags if t) + "*", ""]
    out += direction_block("Client → server", op.get("c2s"))
    out += direction_block("Server → client", op.get("s2c"))
    for key, label in (("server_reply", "Server reply"), ("client_effect", "Client effect"),
                       ("verifier_note", "Verifier note"), ("evidence", "Evidence")):
        if op.get(key):
            out += [f"**{label}:** {op[key]}", ""]
    refs = [f"handler `{op['handler']}`"] if op.get("handler") else []
    sites = op.get("send_sites")
    if sites:
        refs.append("send sites " + ", ".join(f"`{s}`" for s in (sites if isinstance(sites, list) else [sites])))
    if refs:
        out += ["Code: " + "; ".join(refs), ""]
    return out


def render(path):
    data = yaml.safe_load(path.read_text()) or {}
    key = path.stem
    title = TITLES.get(key, key)
    ops = sorted(data.get("opcodes") or [], key=lambda o: o.get("opcode") if isinstance(o.get("opcode"), int) else 1 << 30)
    out = ["---", f'title: "{title}"', "---", "", f"# {title}", "",
           f"Generated from [`contract/{path.name}`](https://github.com/ncwardell/warmonger-revival/blob/main/contract/{path.name}); "
           "edit the YAML, not this page. Offsets are from packet start (payload at +0x10). See [[spec/index|Protocol overview]].", ""]
    comment = header_comment(path)
    if comment:
        out += ["> [!info]- Conventions for this file", *[f"> {line}" for line in comment.splitlines()], ""]
    out += ["## Opcodes", "", "| Opcode | Name | Direction | Confidence | Verified |", "|---|---|---|---|---|"]
    for op in ops:
        anchor = f"{hexop(op.get('opcode'))}-{op.get('name', '')}".lower().replace(" ", "-")  # heading slug
        out.append(f"| [{cell(op.get('opcode'))}](#{anchor}) | {cell(op.get('name'))} | {cell(op.get('direction'))} "
                   f"| {cell(op.get('confidence'))} | {'yes' if op.get('verified') else ''} |")
    out.append("")
    for op in ops:
        out += opcode_section(op)
    flows = data.get("flows") or []
    if flows:
        out += ["## Flows", ""]
        for flow in flows:
            if not isinstance(flow, dict):
                continue
            out += [f"### {flow.get('name', 'flow')}", ""]
            out += [f"{i}. {step}" for i, step in enumerate(flow.get("steps") or [], 1)] + [""]
    rules = data.get("server_rules") or []
    if rules:
        out += ["## Server rules", "", "Decided only by the old server; a new server must design these.", ""]
        for rule in rules:
            if isinstance(rule, dict):
                name = rule.get("name", "rule")
                rest = "; ".join(f"**{k}**: {v}" for k, v in rule.items() if k != "name")
                out.append(f"- **{name}** — {rest}")
            else:
                out.append(f"- {rule}")
        out.append("")
    return key, title, len(ops), sum(1 for o in ops if o.get("verified")), "\n".join(out)


def main(src, dst):
    src, dst = pathlib.Path(src), pathlib.Path(dst)
    dst.mkdir(parents=True, exist_ok=True)
    index = ["---", 'title: "Protocol contract"', "---", "", "# Protocol contract", "",
             "Every opcode the client knows, by system: field layouts, when the client accepts a packet, "
             "what the server must reply, multi-packet flows, and the rules only the old server knew. "
             "Generated from [`contract/`](https://github.com/ncwardell/warmonger-revival/tree/main/contract).", "",
             "| System | Opcodes | Verified |", "|---|---|---|"]
    for path in sorted(src.glob("*.yaml")):
        key, title, count, verified, page = render(path)
        (dst / f"{key}.md").write_text(page)
        index.append(f"| [[contract/{key}\\|{title}]] | {count} | {verified} |")
        print(f"{path} -> {dst / key}.md ({count} opcodes)")
    readme = src / "README.md"
    if readme.exists():
        index += ["", "## Coverage and open work", "", readme.read_text().split("\n", 1)[-1]]
    (dst / "index.md").write_text("\n".join(index) + "\n")


if __name__ == "__main__":
    main(*sys.argv[1:3])
