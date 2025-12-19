import os
import re

TARGET_FILE = os.path.join("maps", "TMA LL Labels.xml")

TARGET_NAME = "TMA_LL_LABELS"
TARGET_COLOUR = "TMA_LL_Colour"

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

        # Check Name="TMA_LL_LABELS"
        if not re.search(rf'Name="{TARGET_NAME}"', attrs):
            return match.group(0)

        # Replace or add CustomColourName
        if re.search(r'CustomColourName="[^"]*"', attrs):
            new_attrs = re.sub(
                r'CustomColourName="[^"]*"',
                f'CustomColourName="{TARGET_COLOUR}"',
                attrs
            )
        else:
            new_attrs = f'{attrs} CustomColourName="{TARGET_COLOUR}"'

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