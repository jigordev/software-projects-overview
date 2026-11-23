#!/usr/bin/env python3
"""Validate finding codes and required fields in a JSON findings array."""
import json, re, sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
PREFIXES = {"ARC":18,"COD":24,"SIM":15,"MNT":20,"SEC":44,"TST":24,"REL":20,
            "PER":26,"SCL":20,"DB":26,"OBS":12,"DOC":15,"DEP":12,"OPS":16,"LLM":24}
REQUIRED = {"id","code","severity","location","detail","fix","evidence","confidence"}

def main():
    if len(sys.argv) != 2:
        print("Usage: validate_findings.py findings.json", file=sys.stderr); return 2
    data = json.loads(Path(sys.argv[1]).read_text(encoding="utf-8"))
    findings = data if isinstance(data, list) else data.get("findings", [])
    errors = []
    for i, f in enumerate(findings):
        missing = REQUIRED - set(f)
        if missing: errors.append(f"[{i}] missing: {', '.join(sorted(missing))}"); continue
        m = re.fullmatch(r"([A-Z]+)-(\d{2})", f["code"])
        if not m or m.group(1) not in PREFIXES or not (1 <= int(m.group(2)) <= PREFIXES[m.group(1)]):
            errors.append(f"[{i}] unknown code: {f['code']}")
        if f["severity"] not in {"S0","S1","S2","S3","S4"}: errors.append(f"[{i}] invalid severity")
        if f["confidence"] not in {"high","medium","low"}: errors.append(f"[{i}] invalid confidence")
        for key, limit in (("detail",500),("fix",300),("evidence",500)):
            if not isinstance(f[key], str) or not f[key].strip() or len(f[key]) > limit:
                errors.append(f"[{i}] invalid {key} length/content")
    if errors:
        print("\\n".join(errors)); return 1
    print(f"OK: {len(findings)} finding(s) validated.")
    return 0

if __name__ == "__main__":
    raise SystemExit(main())
