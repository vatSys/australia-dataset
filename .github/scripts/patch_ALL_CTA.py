import os
import re

TARGET_FILE = os.path.join("maps", "ALL_CTA.xml")

TARGET_MAP_NAME = "ALL_CTA"
TARGET_MAP_COLOUR = "CTA_Colour"

MAP_TAG_RE = re.compile(r'<Map\s+([^>]+)>', re.IGNORECASE)
DASHED_LINE_RE = re.compile(r'(<Line\b[^>]*\bPattern=")Dashed(")', re.IGNORECASE)

def patch_file(path):
    if not os.path.isfile(path):
        print(f"File not found: {path}")
        return

    with open(path, "r", encoding="utf-8") as f:
        content = f.read()

    changed = False

    # --- Patch the Map tag ---
    def map_replacer(match):
        nonlocal changed
        attrs = match.group(1)

        if not re.search(rf'Name="{TARGET_MAP_NAME}"', attrs):
            return match.group(0)

        if re.search(r'CustomColourName="[^"]*"', attrs):
            new_attrs = re.sub(
                r'CustomColourName="[^"]*"',
                f'CustomColourName="{TARGET_MAP_COLOUR}"',
                attrs
            )
        else:
            new_attrs = f'{attrs} CustomColourName="{TARGET_MAP_COLOUR}"'

        changed = True
        return f'<Map {new_attrs}>'

    content = MAP_TAG_RE.sub(map_replacer, content)

    # --- Patch dashed lines to dotted ---
    def line_replacer(match):
        nonlocal changed
        changed = True
        return f'{match.group(1)}Dotted{match.group(2)}'

    content = DASHED_LINE_RE.sub(line_replacer, content)

    # --- Write back if changed ---
    if changed:
        with open(path, "w", encoding="utf-8") as f:
            f.write(content)
        print(f"Patched: {path}")
    else:
        print(f"No changes needed: {path}")

def main():
    patch_file(TARGET_FILE)

if __name__ == "__main__":
    main()