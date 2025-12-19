import os
import re

MAPS_DIR = "maps"

# Regex to match the <Map ...> opening tag
MAP_TAG_REGEX = re.compile(r'<Map\s+([^>]+)>', re.IGNORECASE)

def patch_file(path):
    with open(path, "r", encoding="utf-8") as f:
        content = f.read()

    changed = False

    def replacer(match):
        nonlocal changed
        attributes = match.group(1)

        # Skip if CustomColourName already exists
        if re.search(r'CustomColourName\s*=', attributes, re.IGNORECASE):
            return match.group(0)

        changed = True
        return f'<Map {attributes} CustomColourName="Coast">'

    new_content = MAP_TAG_REGEX.sub(replacer, content, count=1)

    if changed:
        with open(path, "w", encoding="utf-8") as f:
            f.write(new_content)
        print(f"Patched: {path}")
    else:
        print(f"Skipped (already patched): {path}")

def main():
    for root, _, files in os.walk(MAPS_DIR):
        for filename in files:
            if "coast" in filename.lower() and filename.lower().endswith(".xml"):
                full_path = os.path.join(root, filename)
                patch_file(full_path)

if __name__ == "__main__":
    main()