#!/usr/bin/env python3

from datetime import datetime
from pathlib import Path
import os

# Try to get the upstream tag from GitHub Actions, fall back safely
UPSTREAM_TAG = os.getenv("UPSTREAM_TAG", "Unknown")

README_CONTENT = f"""# vatSys Australia Dataset — Dark Theme

This repository contains an **automatically generated dark theme variant** of the official **vatSys Australia dataset**.

> ⚠️ This is **not** the upstream repository.  
> It exists solely to provide a themed alternative.

---

## 🎨 Theme

- **Theme:** Dark
- **Generated:** 2025-12-18
- **Upstream Release:** 2512b
- **Version Format:** `YYMMx-dark` (e.g. `2512b-dark`)

---

## 📥 Installation

1. Download the latest **Dark Theme** release ZIP from the **Releases** page.
2. Extract the ZIP archive.
3. Copy the extracted contents of **profile folder** into: Documents\vatSys Files\Profiles\Australia - Dark
4. Launch **vatSys**.
5. Select the newly installed profile from the profile selection menu.

> ℹ️ If vatSys was running during installation, restart it to ensure the profile appears.

---

## 🔄 Sync & Updates

This repository is automatically synced against the upstream dataset:

- New upstream releases are detected on a schedule
- If a dark-themed release already exists, no action is taken
- Patches are applied deterministically to ensure consistent output

There are **no manual edits** to data files in this repository.

---

## 🛠 Patch Scripts

The repository includes Python patch scripts for automated modifications to XML map files in the `maps/` folder.

### Patch Scripts Included

1. **`patch_coast.py`** – Adds `CustomColourName="Coast"` to `<Map>` tags in files containing `coast` in their names.
2. **`patch_asmgcs.py`** – Updates `ASMGCS.xml` map names with correct `CustomColourName` values, handling changes to existing values.
3. **`patch_all_cta.py`** – Adds `CustomColourName="ALL_CTA"` and converts line patterns from `Dashed` to `Dotted` in `ALL_CTA.xml`.
4. **`split_rwy_maps.py`** – Splits runway XML files (any file with `RWY` in the name) into separate map sections (`_Centreline`, `_SIDs`, `_STARs`, `_Symbols`, `_Airspace`, `_Names`) and overwrites the originals. Sections are only written if content exists; unlabelled lines are skipped.

### Usage

Run any script with:

```bash
python <script_name>.py
```

> ⚠️ Backup XML files before running patches as they overwrite originals in-place.

---

## ⬇️ Downloads

### GitHub Releases (Recommended)

Download the latest themed dataset from the **Releases** page:

- Each release corresponds to an upstream version
- Assets include a pre-packaged ZIP ready for vatSys
- Once installed this profile should automatically update via downloads from free hosting provided by alwaysdata.com

---

## 📦 Contents

The dataset includes:
- Profile configuration
- Colour definitions adjusted for dark theme usage
- Supporting metadata required by vatSys automated updates
- Patch scripts for automated XML modifications

---

## ⚖️ Attribution & Disclaimer

- Original dataset © vatSys Australia contributors
- Theme modifications and patch scripts are provided independently
- This project is **not affiliated with or endorsed by vatSys, VATSIM or VATPAC**

All credit for data accuracy and structure belongs to the upstream authors.

---

## ⚠️ Disclaimer & Limitation of Liability

This dataset and patch scripts are provided **as-is**, without warranty of any kind, express or implied.

By using this dataset, you acknowledge and agree that:

- You use it **at your own risk**
- The maintainers accept **no responsibility** for errors, omissions, or inaccuracies
- No liability is accepted for any loss, damage, or disruption arising from its use
- It is your responsibility to verify suitability for your intended purpose

This applies to both the dataset itself, any automated processes used to generate it, patch scripts, and/or automatic updates to the profile.

---

## 🛠 Automation Details

This repository is maintained via GitHub Actions:
- Scheduled sync every few hours
- Tag-based release detection
- Idempotent patching to prevent duplicate releases
- Patch scripts are executed automatically to ensure consistency

---

If you encounter issues specific to the **dark theme** or the patch scripts, please open an issue in **this repository**.
"""

def main():
    readme_path = Path("README.md")
    readme_path.write_text(README_CONTENT, encoding="utf-8")
    print("README.md successfully regenerated.")

if __name__ == "__main__":
    main()
