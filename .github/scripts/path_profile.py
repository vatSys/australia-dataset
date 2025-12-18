#!/usr/bin/env python3
import xml.etree.ElementTree as ET
import sys

FILE_PATH = "Profile.xml"

NEW_PROFILE = {
    "Name": "Australia-Dark",
    "FullName": "Eurocat Australia (YMMM/YBBB) - Dark",
}

NEW_VERSION_ATTRS = {
     "UpdateURL": "http://vatsys-au-dark.alwaysdata.net/data"
    # Optional overrides — comment out if you want upstream to control these
    # "Revision": "dark",
 }
# --- Preserve original XML declaration ---
with open(FILE_PATH, "r", encoding="utf-8") as f:
    lines = f.readlines()

xml_declaration = ""
if lines and lines[0].startswith("<?xml"):
    xml_declaration = lines[0].rstrip("\n")
    
# Parse XML
tree = ET.parse(FILE_PATH)
root = tree.getroot()  # root IS the <Profile> element

# Update Profile attributes
for attr, value in NEW_PROFILE.items():
    root.set(attr, value)

# Find Version element (direct child of Profile)
version = root.find("Version")
if version is None:
    sys.exit("ERROR: <Version> element not found inside <Profile>")

# Update Version attributes
for attr, value in NEW_VERSION_ATTRS.items():
    version.set(attr, value)

# Write XML WITHOUT declaration
tree.write(FILE_PATH, encoding="utf-8", xml_declaration=False)

# Re-add original declaration
if xml_declaration:
    with open(FILE_PATH, "r", encoding="utf-8") as f:
        content = f.read()

    with open(FILE_PATH, "w", encoding="utf-8") as f:
        f.write(xml_declaration + "\n" + content)

print("Profile.xml patched successfully")
