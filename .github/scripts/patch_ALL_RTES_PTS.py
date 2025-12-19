import os
import re

TARGET_FILE = os.path.join("maps", "ALL_RTES_PTS.xml")

# Define multiple target names and their corresponding colours
TARGETS = {
    "ALL_ROUTES_HIGH": "ALL_ROUTES_HIGH_COLOUR",
    "ALL_ROUTES_LOW": "ALL_ROUTES_LOW_COLOUR",
    "ALL_POINTS_HIGH": "ALL_POINTS_HIGH_COLOUR",
    "ALL_POINTS_LOW": "ALL_POINTS_LOW_COLOUR"

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

        # Check if any target name matches
        for target_name, target_colour in TARGETS.items():
            if re.search(rf'Name="{re.escape(target_name)}"', attrs):
                # Replace or add CustomColourName
                if re.search(r'CustomColourName="[^"]*"', attrs):
                    new_attrs = re.sub(
                        r'CustomColourName="[^"]*"',
                        f'CustomColourName="{target_colour}"',
                        attrs
                    )
                else:
                    new_attrs = f'{attrs} CustomColourName="{target_colour}"'

                changed = True
                return f'<Map {new_attrs}>'

        # No match, return original
        return match.group(0)

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
