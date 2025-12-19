import os
import re

MAPS_ROOT = "maps"

RUNWAY_RE = re.compile(r'<Runway\b.*?</Runway>', re.DOTALL | re.IGNORECASE)
LINE_RE = re.compile(r'<Line\b.*?</Line>', re.DOTALL | re.IGNORECASE)
SYMBOL_RE = re.compile(r'<Symbol\b.*?</Symbol>', re.DOTALL | re.IGNORECASE)
LABEL_RE = re.compile(r'<Label\b.*?</Label>', re.DOTALL | re.IGNORECASE)

def emit_map(name, priority, center, colour, content):
    if not content:
        return ""
    return f'''
  <Map Type="System" Name="{name}" Priority="{priority}" Center="{center}" CustomColourName="{colour}">
{chr(10).join(content)}
  </Map>'''

def split_rwy_file(path):
    filename = os.path.basename(path)

    if "RWY" not in filename.upper() or not filename.lower().endswith(".xml"):
        return

    with open(path, "r", encoding="utf-8") as f:
        src = f.read()

    center_match = re.search(r'Center="([^"]+)"', src)
    if not center_match:
        print(f"⚠️  Skipped (no Center): {path}")
        return

    center = center_match.group(1)
    base_name = filename.replace(".xml", "")

    runways = RUNWAY_RE.findall(src)
    symbols = SYMBOL_RE.findall(src)
    labels = LABEL_RE.findall(src)

    airspace = []
    for line in LINE_RE.findall(src):
        if 'Name="(' in line and "RWY" in line:
            airspace.append(line)

    sids = []
    stars = []

    current_section = None
    buffer = []
    collecting = False

    for line in src.splitlines():
        if "<!--SIDs-->" in line:
            current_section = "SIDs"
            continue
        if "<!--STARs-->" in line:
            current_section = "STARs"
            continue

        if "<Line" in line:
            buffer = [line]
            collecting = True
            continue

        if collecting:
            buffer.append(line)
            if "</Line>" in line:
                block = "\n".join(buffer)
                if current_section == "SIDs":
                    sids.append(block)
                elif current_section == "STARs":
                    stars.append(block)
                collecting = False
                buffer = []

    if not runways:
        print(f"⚠️  Skipped (no Runways): {path}")
        return

    sections = [
        emit_map(f"{base_name}_Centreline", 1, center, "Centreline", runways),
        emit_map(f"{base_name}_SIDs", 1, center, "SIDs", sids),
        emit_map(f"{base_name}_STARs", 1, center, "STARs", stars),
        emit_map(f"{base_name}_Symbols", 1, center, "Airways_Symbols", symbols),
        emit_map(f"{base_name}_Airspace", 1, center, "Airspace", airspace),
        emit_map(f"{base_name}_Names", 2, center, "Names", labels),
    ]

    output = f'''<?xml version="1.0" encoding="utf-8"?>
<Maps>
{''.join(sections)}
</Maps>
'''

    # 🔁 Overwrite original file
    with open(path, "w", encoding="utf-8") as f:
        f.write(output)

    print(f"✔ Rewritten (empty sections skipped): {path}")

def main():
    for root, _, files in os.walk(MAPS_ROOT):
        for file in files:
            if "RWY" in file.upper() and file.lower().endswith(".xml"):
                split_rwy_file(os.path.join(root, file))

if __name__ == "__main__":
    main()
