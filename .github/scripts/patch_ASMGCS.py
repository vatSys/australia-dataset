import os
import re

TARGET_FILE = os.path.join("maps", "ASMGCS.xml")

# Map Name -> Desired CustomColourName
PATCHES = {
    "ASMGCS_RWY_ALL": "RWY",
    "ASMGCS_RWY_RSM": "RWY_RSM",
}

MAP_TAG_RE = re.compile(r'<Map\s+([^>]+)>', re.IGNORECASE)

def patch_file(path):
    if not os.path.isfile(path):
        print(f"File not found: {path}")
        return

    with open(path, "r", encoding="utf-8") as f:
        content = f.read()

    changed = False

    def replacer(match):
        nonlocal changed
        attrs = match.group(1)

        # Extract Name="..."
        name_match = re.search(r'Name="([^"]+)"', attrs)
        if not name_match:
            return match.group(0)

        map_name = name_match.group(1)

        if map_name not in PATCHES:
            return match.group(0)

        desired_colour = PATCHES[map_name]

        # Replace existing CustomColourName if present
        if re.search(r'CustomColourName="[^"]*"', attrs):
            new_attrs = re.sub(
                r'CustomColourName="[^"]*"',
                f'CustomColourName="{desired_colour}"',
                attrs
            )
        else:
            # Otherwise, add it
            new_attrs = f'{attrs} CustomColourName="{desired_colour}"'

        changed = True
        return f'<Map {new_attrs}>'

    new_content = MAP_TAG_RE.sub(replacer, content)

    if changed:
        with open(path, "w", encoding="utf-8") as f:
            f.write(new_content)
        print(f"Patched: {path}")
    else:
        print(f"No changes needed: {path}")

def main():
    patch_file(TARGET_FILE)

if __name__ == "__main__":
    main()