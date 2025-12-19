#!/usr/bin/env python3
import xml.etree.ElementTree as ET
import sys

FILE_PATH = "Colours.xml"

# Key = (id, Use), Value = dict of new values
COLOUR_UPDATES = {



    ## Window and Control Backgrounds
    # Air Situation Display Background
    ("ASDBackground", "ASD Backgrounds"): {"Name": "VeryDarkGrey", "R": "15", "G": "15", "B": "15"},
    # Ground situation display backgound
    ("GroundBackground", "A-SMGCS Background"): {"Name": "Black", "R": "15", "G": "15", "B": "15"},
    # Generic Window Background
    ("WindowBackground", "Window Backgrounds"): {"Name": "VeryDarkGrey", "R": "15", "G": "15", "B": "15"},
    # Warning colour used in menu, button and window backgrounds
    ("WindowWarning", "Warning Indications in Windows"): {"Name": "BrightYellow", "R": "255", "G": "255", "B": "0"},
    # mergency colour used in menu, button and window backgrounds
    ("WindowEmergency", "Emergency Indications in Windows"): {"Name": "StrongRed", "R": "209", "G": "46", "B": "46"},
    # Selected (Toggled) menu, button and scrollbar backgrounds
    ("WindowButtonSelected", "Selected Window Button Background"): {"Name": "MediumGrey", "R": "110", "G": "110", "B": "110"},
    # Depressed (button) or hover (menu item) backgrounds
    ("WindowButtonDepressed", "Depressed Window Button Background"): {"Name": "SlateGrey", "R": "60", "G": "71", "B": "71"},
    # Selected Text
    ("HighlightedText", "Highlighted Text"): {"Name": "Cyan", "R": "0", "G": "255", "B": "255"},
    # Font of interactive items
    ("InteractiveText", "InteractiveText"): {"Name": "MediumGrey", "R": "110", "G": "110", "B": "110"},
    # Font of non-interactive items
    ("NonInteractiveText", "Non-Interactive Text"): {"Name": "DarkGrey", "R": "90", "G": "90", "B": "90"},
    # Generic font
    ("GenericText", "Window Text"): {"Name": "MediumGrey", "R": "110", "G": "110", "B": "110"},
    # Background of strips
    ("StripBackground", "Strip Backgrounds"): {"Name": "VeryDarkGrey", "R": "15", "G": "15", "B": "15"},
    # Strip Font
    ("StripText", "Strip Text"): {"Name": "LightGrey", "R": "170", "G": "170", "B": "170"},
    # List Separator Bars
    ("ListSeparator", "List Separator Bar"): {"Name": "DarkGrey", "R": "30", "G": "30", "B": "30"},
    # List Separator Bars when Selected
    ("ListSeparatorSelected", "List Separator Bar Selected"): {"Name": "SlateGrey", "R": "60", "G": "71", "B": "71"},
    # Generic CPDLC message background
    ("CPDLCMessageBackground", "CPDLC Background"): {"Name": "Cream", "R": "230", "G": "210", "B": "190"},
    # Downlink Messages and label item
    ("CPDLCDownlink", "CPDLC Downlink Highlight and Messages"): {"Name": "DarkGreen", "R": "0", "G": "105", "B": "0"},
    # Uplink Messages and label item
    ("CPDLCUplink", "CPDLC Uplink Highlight and Messages"): {"Name": "DarkBlue", "R": "0", "G": "0", "B": "105"},
    # Freetext Messages
    ("CPDLCFreetext", "CPDLC Freetext Messages"): {"Name": "VeryDarkGrey", "R": "26", "G": "26", "B": "26"},
    # CPDLC Editor Window send button
    ("CPDLCSendButton", "CPDLC Hot-Send Button"): {"Name": "BrightBlue", "R": "101", "G": "101", "B": "255"},
    # Border colour of focused popup Air/Ground Windows
    ("PopupASDWindowBorderFocused", "Popup ASD Window borders when focused"): {"Name": "TealGrey", "R": "130", "G": "155", "B": "155"},
    # Border colour of Generic windows
    ("WindowBorder", "All Window Borders"): {"Name": "MediumGrey", "R": "110", "G": "110", "B": "110"},

    ## MAPS
    # System maps and default
    ("PrimaryMap", "System Maps"): {"Name": "DarkGrey", "R": "67", "G": "137", "B": "137"},
    # System2 maps
    ("SecondaryMap", "Alternative System Map"): {"Name": "BlueGrey", "R": "42", "G": "50", "B": "52"},
    # REST_NTZ_DAIW, TDA and Supervisor maps
    ("PRDArea", "Restricted/Danger Areas"): {"Name": "Red", "R": "53", "G": "4", "B": "4"},
    #  Local_Private and Global_Private maps (not currently used)
    ("UserMap", "Custom Maps and Text"): {"Name": "BrightYellow", "R": "235", "G": "235", "B": "0"},
    # Filled maps
    ("Infill", "Filled Area Map"): {"Name": "VeryDarkGrey", "R": "10", "G": "10", "B": "10"},
    # Ground Situation Displays only
    ("GroundRunway", "A-SMGCS Runway"): {"Name": "DarkSlateGrey", "R": "115", "G": "115", "B": "115"},
    # Ground Situation Displays only
    ("GroundTaxiway", "A-SMGCS Taxiway"): {"Name": "DarkGrey", "R": "50", "G": "50", "B": "50"},
    # Ground Situation Displays only
    ("GroundApron", "A-SMGCS Apron"): {"Name": "DarkGreen", "R": "75", "G": "75", "B": "75"},
    # Ground Situation Displays only
    ("GroundBuilding", "A-SMGCS Building"): {"Name": "MediumGrey", "R": "0", "G": "64", "B": "64"},
    # Ground Situation Displays only
    ("GroundOther", "A-SMGCS Information / Other"): {"Name": "LightGrey", "R": "150", "G": "150", "B": "150"},

    ## TRACK, LABELS, STRIPS
    # FDR has not been activated (strip state only)
    ("Preactive", "Preactive Tracks and Strips"): {"Name": "White", "R": "202", "G": "205", "B": "169"},
    # Controlled by you
    ("Jurisdiction", "Jurisdiction"): {"Name": "MediumGreen", "R": "90", "G": "190", "B": "150"},
    # Controlled by another controller that is also one of your selected sectors 
    ("GhostJurisdiction", "GhostJurisdiction"): {"Name": "LightGreen", "R": "89", "G": "209", "B": "65"},
    # Handover Out accepted
    ("PostJurisdiction", "PostJurisdiction"): {"Name": "White", "R": "202", "G": "205", "B": "169"},

    ("JurisdictionIQL", "JurisdictionIQL"): {"Name": "BrightGreen", "R": "0", "G": "255", "B": "0"},
    # Handoff proposed to you
    ("Handover", "HandOver"): {"Name": "MediumGreen", "R": "190", "G": "100", "B": "95"},
    # Soon to affect your sectors 
    ("Announced", "Announced"): {"Name": "BrightCyan", "R": "70", "G": "255", "B": "255"},

    ("NonJurisdictionIQL", "NonJurisdictionIQL"): {"Name": "White", "R": "202", "G": "205", "B": "169"},
    # All other tracks
    ("NonJurisdiction", "Non Jurisdiction Tracks and Strips"): {"Name": "White", "R": "202", "G": "205", "B": "169"},

    ("NonJurisdictionLabel", "Non Jurisdiction Labels"): {"Name": "White", "R": "202", "G": "205", "B": "169"},

    ("CFLHighlight", "New CFL Selection"): {"Name": "White", "R": "255", "G": "255", "B": "255"},

    ("IdentFlash", "SPI"): {"Name": "Cyan", "R": "0", "G": "255", "B": "255"},
    
    ("Route", "Graphic Route"): {"Name": "Lavender", "R": "196", "G": "171", "B": "196"},

    ("PostJurisdictionFlash", "Post Jurisdiction Transfer Flashing"): {"Name": "White", "R": "255", "G": "200", "B": "150"},

    ("GroundUnknown", "A-SMGCS Aircraft"): {"Name": "Orange", "R": "255", "G": "156", "B": "55"},

    ("GroundArrival", "A-SMGCS Arrival"): {"Name": "LightBuff", "R": "255", "G": "255", "B": "160"},

    ("GroundDeparture", "A-SGCMS Departure"): {"Name": "LightBlue", "R": "139", "G": "220", "B": "243"},

    ("GroundLocal", "A-SGCMS Local"): {"Name": "BrightPink", "R": "255", "G": "100", "B": "255"},

    ("Emergency", "Emergency Indications"): {"Name": "StrongRed", "R": "209", "G": "46", "B": "46"},

    ("Warning", "Warning Indications"): {"Name": "BrightYellow", "R": "255", "G": "255", "B": "0"},


    ## TOOLS 
    ("StaticTools", "BRL,PETO,NonRVSM,LATC,ETO"): {"Name": "PaleOrange", "R": "255", "G": "230", "B": "180"},
    ("DynamicTools", "Dynamic Tool In Use"): {"Name": "OffWhite", "R": "255", "G": "230", "B": "230"},
 

    ## Arrival Manager
    ("Frozen", "Arrival Manager Frozen Flight"): {"Name": "DarkRed", "R": "120", "G": "0", "B": "0"},
    ("Stable", "Arrival Manager Stable Flight"): {"Name": "White", "R": "255", "G": "255", "B": "255"},
    ("SuperStable", "Arrival Manager Super Stable Flight"): {"Name": "LightBlue", "R": "100", "G": "210", "B": "255"},
    ("Unstable", "Arrival Manager Unstable Flight"): {"Name": "YellowOrange", "R": "255", "G": "240", "B": "0"},
    ("DelayMinor", "Arrival Manager Minor Delay"): {"Name": "Cyan", "R": "0", "G": "235", "B": "235"},
    ("DelayMajor", "Arrival Manager Major Delay"): {"Name": "BrightYellow", "R": "235", "G": "235", "B": "0"},
    
    ## VSCS
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


    ## CUSTOM
    ("Custom", "Area QNH Map"): {"Name": "OliveYellow", "R": "180", "G": "180", "B": "0"},
    ("Custom", "Runway Numbers"): {"Name": "RWY",  "R": "255", "G": "255", "B": "0"},
    ("Custom", "RRSM Markers"): {"Name": "RWY_RSM", "R": "255", "G": "255", "B": "0"},
    ("Custom", "Coast"): {"Name": "Coast", "R": "60", "G": "78", "B": "99"},
    ("Custom", "CTA_Colour"): {"Name": "CTA_Colour", "R": "15", "G": "45", "B": "35"},
    ("Custom", "TMA_LL_Colour"): {"Name": "TMA_LL_Colour", "R": "15", "G": "45", "B": "35"},

    ("Custom", "Centreline"): {"Name": "Centreline", "R": "48", "G": "48", "B": "48"},
    ("Custom", "SIDs"): {"Name": "SIDs", "R": "55", "G": "55", "B": "0"},
    ("Custom", "STARs"): {"Name": "STARs", "R": "0", "G": "70", "B": "70"},
    ("Custom", "Ariways_Symbols"): {"Name": "Ariways_Symbols", "R": "43", "G": "136", "B": "97"},
    ("Custom", "Airspace"): {"Name": "Airspace", "R": "15", "G": "45", "B": "35"},
    ("Custom", "Names"): {"Name": "Names", "R": "85", "G": "85", "B": "85"},

    ("Custom", "ALL_ROUTES_HIGH_COLOUR"): {"Name": "ALL_ROUTES_HIGH_COLOUR", "R": "85", "G": "85", "B": "85"},
    ("Custom", "ALL_ROUTES_LOW_COLOUR"): {"Name": "ALL_ROUTES_LOW_COLOUR", "R": "85", "G": "85", "B": "85"},
    ("Custom", "ALL_POINTS_HIGH_COLOUR"): {"Name": "ALL_POINTS_HIGH_COLOUR", "R": "85", "G": "85", "B": "85"},
    ("Custom", "ALL_POINTS_LOW_COLOUR"): {"Name": "ALL_POINTS_LOW_COLOUR", "R": "85", "G": "85", "B": "85"},
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
