#!/usr/bin/env python3
import xml.etree.ElementTree as ET
import sys

FILE_PATH = "Colours.xml"

# Key = (id, Use), Value = dict of new values
COLOUR_UPDATES = {
    ("GenericText", "Window Text"): {"Name": "MediumGrey", "R": "110", "G": "110", "B": "110"},
    ("InteractiveText", "InteractiveText"): {"Name": "MediumGrey", "R": "110", "G": "110", "B": "110"},
    ("StripText", "Strip Text"): {"Name": "LightGrey", "R": "220", "G": "220", "B": "220"},
    ("PopupASDWindowBorderFocused", "Popup ASD Window borders when focused"): {"Name": "TealGrey", "R": "130", "G": "155", "B": "155"},
    ("StripBackground", "Strip Backgrounds"): {"Name": "VeryDarkGrey", "R": "22", "G": "22", "B": "22"},
    ("ListSeparator", "List Separator Bar"): {"Name": "DarkGrey", "R": "30", "G": "30", "B": "30"},
    ("ListSeparatorSelected", "List Separator Bar Selected"): {"Name": "SlateGrey", "R": "60", "G": "71", "B": "71"},
    ("WindowBackground", "Window Backgrounds"): {"Name": "VeryDarkGrey", "R": "30", "G": "30", "B": "30"},
    ("WindowButtonDepressed", "Depressed Window Button Background"): {"Name": "SlateGrey", "R": "60", "G": "71", "B": "71"},
    ("WindowButtonSelected", "Selected Window Button Background"): {"Name": "MediumGrey", "R": "110", "G": "110", "B": "110"},
    ("WindowEmergency", "Emergency Indications in Windows"): {"Name": "StrongRed", "R": "209", "G": "46", "B": "46"},
    ("WindowWarning", "Warning Indications in Windows"): {"Name": "BrightYellow", "R": "255", "G": "255", "B": "0"},
    ("Custom", "Area QNH Map"): {"Name": "OliveYellow", "R": "180", "G": "180", "B": "0"},
    ("Custom", "Runway Numbers"): {"Name": "White", "R": "255", "G": "255", "B": "255"},
    ("Custom", "RRSM Markers"): {"Name": "OffWhite", "R": "240", "G": "240", "B": "240"},
    ("Preactive", "Preactive Tracks and Strips"): {"Name": "White", "R": "255", "G": "255", "B": "255"},
    ("HighlightedText", "Highlighted Text"): {"Name": "Cyan", "R": "0", "G": "255", "B": "255"},
    ("CPDLCMessageBackground", "CPDLC Background"): {"Name": "Cream", "R": "230", "G": "210", "B": "190"},
    ("CPDLCDownlink", "CPDLC Downlink Highlight and Messages"): {"Name": "DarkGreen", "R": "0", "G": "105", "B": "0"},
    ("CPDLCUplink", "CPDLC Uplink Highlight and Messages"): {"Name": "DarkBlue", "R": "0", "G": "0", "B": "105"},
    ("CPDLCFreetext", "CPDLC Freetext Messages"): {"Name": "VeryDarkGrey", "R": "26", "G": "26", "B": "26"},
    ("Emergency", "Emergency Indications"): {"Name": "StrongRed", "R": "209", "G": "46", "B": "46"},
    ("Warning", "Warning Indications"): {"Name": "BrightYellow", "R": "255", "G": "255", "B": "0"},
    ("VSCSBackground", "VSCS Background"): {"Name": "DarkGrey", "R": "30", "G": "30", "B": "30"},
    ("VSCSHotline", "Closed VSCS Hotlines"): {"Name": "BrightYellow", "R": "235", "G": "235", "B": "0"},
    ("VSCSOpenHotline", "Open VSCS Hotlines"): {"Name": "BrightGreen", "R": "0", "G": "235", "B": "0"},
    ("VSCSColdline", "VSCS Closed Coldlines"): {"Name": "Cyan", "R": "0", "G": "235", "B": "235"},
    ("VSCSOpenColdline", "VSCS Open and (flashing) Ringing Coldlines"): {"Name": "DarkPurple", "R": "91", "G": "68", "B": "122"},
    ("VSCSActiveFrequency", "VSCS Frequencies that can be transmitted on"): {"Name": "MediumGreen", "R": "85", "G": "175", "B": "120"},
    ("VSCSReceivingFrequency", "VSCS Frequencies are receiving a transmission"): {"Name": "White", "R": "255", "G": "255", "B": "255"},
    ("VSCSFrequencyWarning", "VSCS Frequencies that are receive only or without voice"): {"Name": "BrightYellow", "R": "235", "G": "235", "B": "0"},
    ("VSCSButtonDepressed", "VSCS Generic Buttons"): {"Name": "DarkGrey", "R": "70", "G": "70", "B": "70"},
    ("VSCSButtonSelected", "VSCS Buttons that are selected / highlighted"): {"Name": "Fuchsia", "R": "241", "G": "178", "B": "225"},
    ("NonInteractiveText", "Non-Interactive Text"): {"Name": "DarkGrey", "R": "90", "G": "90", "B": "90"},
    ("ASDBackground", "ASD Backgrounds"): {"Name": "VeryDarkGrey", "R": "25", "G": "25", "B": "25"},
    ("CPDLCSendButton", "CPDLC Hot-Send Button"): {"Name": "BrightBlue", "R": "101", "G": "101", "B": "255"},
    ("GroundBackground", "A-SMGCS Background"): {"Name": "Black", "R": "0", "G": "0", "B": "0"},
    ("Jurisdiction", "Jurisdiction"): {"Name": "MediumGreen", "R": "89", "G": "209", "B": "65"},
    ("GhostJurisdiction", "GhostJurisdiction"): {"Name": "LightGreen", "R": "89", "G": "209", "B": "65"},
    ("PostJurisdiction", "PostJurisdiction"): {"Name": "White", "R": "255", "G": "255", "B": "255"},
    ("JurisdictionIQL", "JurisdictionIQL"): {"Name": "BrightGreen", "R": "0", "G": "255", "B": "0"},
    ("Handover", "HandOver"): {"Name": "MediumGreen", "R": "89", "G": "209", "B": "65"},
    ("Announced", "Announced"): {"Name": "BrightCyan", "R": "70", "G": "255", "B": "255"},
    ("NonJurisdictionIQL", "NonJurisdictionIQL"): {"Name": "White", "R": "255", "G": "255", "B": "255"},
    ("NonJurisdiction", "Non Jurisdiction Tracks and Strips"): {"Name": "White", "R": "255", "G": "255", "B": "255"},
    ("NonJurisdictionLabel", "Non Jurisdiction Labels"): {"Name": "White", "R": "255", "G": "255", "B": "255"},
    ("CFLHighlight", "New CFL Selection"): {"Name": "White", "R": "255", "G": "255", "B": "255"},
    ("IdentFlash", "SPI"): {"Name": "Cyan", "R": "0", "G": "255", "B": "255"},
    ("Route", "Graphic Route"): {"Name": "Lavender", "R": "196", "G": "171", "B": "196"},
    ("StaticTools", "BRL,PETO,NonRVSM,LATC,ETO"): {"Name": "PaleOrange", "R": "255", "G": "230", "B": "180"},
    ("PostJurisdictionFlash", "Post Jurisdiction Transfer Flashing"): {"Name": "White", "R": "255", "G": "255", "B": "255"},
    ("GroundArrival", "A-SMGCS Arrival"): {"Name": "LightBuff", "R": "255", "G": "255", "B": "160"},
    ("GroundUnknown", "A-SMGCS Aircraft"): {"Name": "Orange", "R": "255", "G": "156", "B": "55"},
    ("GroundDeparture", "A-SGCMS Departure"): {"Name": "LightBlue", "R": "139", "G": "220", "B": "243"},
    ("GroundLocal", "A-SGCMS Local"): {"Name": "BrightPink", "R": "255", "G": "100", "B": "255"},
    ("PRDArea", "Restricted/Danger Areas"): {"Name": "Red", "R": "255", "G": "59", "B": "20"},
    ("UserMap", "Custom Maps and Text"): {"Name": "BrightYellow", "R": "235", "G": "235", "B": "0"},
    ("PrimaryMap", "System Maps"): {"Name": "DarkGrey", "R": "67", "G": "137", "B": "137"},
    ("Infill", "Filled Area Map"): {"Name": "VeryDarkGrey", "R": "10", "G": "10", "B": "10"},
    ("SecondaryMap", "Alternative System Map"): {"Name": "BlueGrey", "R": "42", "G": "50", "B": "52"},
    ("GroundRunway", "A-SMGCS Runway"): {"Name": "DarkSlateGrey", "R": "33", "G": "60", "B": "63"},
    ("GroundTaxiway", "A-SMGCS Taxiway"): {"Name": "DarkGrey", "R": "28", "G": "30", "B": "34"},
    ("GroundApron", "A-SMGCS Apron"): {"Name": "DarkGreen", "R": "0", "G": "40", "B": "0"},
    ("GroundBuilding", "A-SMGCS Building"): {"Name": "MediumGrey", "R": "90", "G": "90", "B": "90"},
    ("GroundOther", "A-SMGCS Information / Other"): {"Name": "LightGrey", "R": "150", "G": "150", "B": "150"},
    ("DynamicTools", "Dynamic Tool In Use"): {"Name": "OffWhite", "R": "255", "G": "230", "B": "230"},
    ("Frozen", "Arrival Manager Frozen Flight"): {"Name": "DarkRed", "R": "120", "G": "0", "B": "0"},
    ("Stable", "Arrival Manager Stable Flight"): {"Name": "White", "R": "255", "G": "255", "B": "255"},
    ("SuperStable", "Arrival Manager Super Stable Flight"): {"Name": "LightBlue", "R": "100", "G": "210", "B": "255"},
    ("Unstable", "Arrival Manager Unstable Flight"): {"Name": "YellowOrange", "R": "255", "G": "240", "B": "0"},
    ("DelayMinor", "Arrival Manager Minor Delay"): {"Name": "Cyan", "R": "0", "G": "235", "B": "235"},
    ("DelayMajor", "Arrival Manager Major Delay"): {"Name": "BrightYellow", "R": "235", "G": "235", "B": "0"},
    ("WindowBorder", "All Window Borders"): {"Name": "MediumGrey", "R": "110", "G": "110", "B": "110"},
}

# Register the xsi namespace so it is preserved
ET.register_namespace('xsi', 'http://www.w3.org/2001/XMLSchema-instance')

# --- Preserve first TWO lines exactly ---
with open(FILE_PATH, "r", encoding="utf-8") as f:
    original_lines = f.readlines()

if len(original_lines) < 2:
    sys.exit("ERROR: Colours.xml has fewer than 2 lines")

original_header = original_lines[:2]

tree = ET.parse(FILE_PATH)
root = tree.getroot()

for (colour_id, use_val), values in COLOUR_UPDATES.items():
    # Look for a colour with the same id AND <Use> text
    colour_elem = None
    for elem in root.findall(f".//Colour[@id='{colour_id}']"):
        use_elem = elem.find("Use")
        if use_elem is not None and use_elem.text == use_val:
            colour_elem = elem
            break

    if colour_elem is None:
        # Not found → create new
        colour_elem = ET.Element("Colour", {"id": colour_id})
        use_elem = ET.SubElement(colour_elem, "Use")
        use_elem.text = use_val
        root.append(colour_elem)

    # Update or add Name/R/G/B
    for tag, text in values.items():
        sub_elem = colour_elem.find(tag)
        if sub_elem is None:
            sub_elem = ET.SubElement(colour_elem, tag)
        sub_elem.text = text
        
# Write XML with declaration
tree.write(FILE_PATH, encoding="utf-8", xml_declaration=True)

# Re-add preserved header
with open(FILE_PATH, "r", encoding="utf-8") as f:
    new_lines = f.readlines()

with open(FILE_PATH, "w", encoding="utf-8") as f:
    f.writelines(original_header)
    f.writelines(new_lines[2:])

print("Colours.xml patched successfully")
