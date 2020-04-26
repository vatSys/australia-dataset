# Maps
Maps are what the Air Situation Display uses to display background information to the user of the client.

Each XML file must contain one `<Maps>` element, which may define multiple `<Map>` elements. Each `<Map>` are individually selectable within vatSys.

Folder structure within the `vatSys Files\Maps\\` directory is preserved by the Maps menu within vatSys.

# Map Element

The Map element has the following attributes and children elements.

#### Type
Each `Map` element may have one `Type` attribute from the following:

```
        {
            System,
            System2,
            Flex,
            Filled, 
            Local_Private,
            Global_Private,
            Supervisor,
            TDA,
            REST_NTZ_DAIW,
            Ground_RWY,
            Ground_TWY,
            Ground_APR,
            Ground_BLD,
            Ground_BAK
        }
```

The type primarily will affect the colour vatSys uses to paint the map. Colours are defined in Colours.xml.

#### Name
The title of the Map (as displayed to the user).

#### Priority
An integer specifying the z-axis layering of the map, 0 being drawn on top of everything else.

`PRIORITY_HIGHEST = 0`

#### Center
An approximate center point of the map, used to deconflict in the event of multiple Waypoints with the same name.

## Line Element

## Symbol Element

## Label Element
Each `<Label>` element of a map can have attributes `HasLeader="bool"` and `LabelOrientation="enum"` - these attributes specify if there is a line drawn from the point location to the text label and which compass direction or not.

Each `<Label>` can have multiple `<Point>` children. Each Point can have the attribute `Name="string"` (which is displayed as the label text) and the InnerText is either an otherwise defined waypoint/navaid/airport or latlong in standard format of where to place the label. If you omit Name the name is generated from the InnerText. 

`<Map>` element attribute Type changes the colour of the map, and of course you've seen Pattern already.