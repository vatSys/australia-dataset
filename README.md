# vatsys-australia-dataset
Default profile dataset for vatSys

**`Profile.xml` must be updated for each release**

## Data Definition Hierarchy

The definition of all WAYPOINT, NAVAID, AIRPORT, SID & STAR names referenced by vatSys XML files are searched for in the following order:

1. Airspace.xml
2. Navigraph Data

## Lat Long Format

vatSys accepts coordinates in any valid [ISO 6709 format](https://en.wikipedia.org/wiki/ISO_6709).

```
Latitude and Longitude in Degrees:
    ±DD.DDDD±DDD.DDDD         (eg +12.345-098.765)
Latitude and Longitude in Degrees and Minutes:
    ±DDMM.MMMM±DDDMM.MMMM     (eg +1234.56-09854.321)
Latitude and Longitude in Degrees, Minutes and Seconds:
    ±DDMMSS.SSSS±DDDMMSS.SSSS (eg +123456.7-0985432.1)
Latitude, Longitude (in Degrees) and Altitude:
    ±DD.DDDD±DDD.DDDD±AAA.AAA         (eg +12.345-098.765+15.9)
Latitude, Longitude (in Degrees and Minutes) and Altitude:
    ±DDMM.MMMM±DDDMM.MMMM±AAA.AAA     (eg +1234.56-09854.321+15.9)
Latitude, Longitude (in Degrees, Minutes and Seconds) and Altitude:
    ±DDMMSS.SSSS±DDDMMSS.SSSS±AAA.AAA (eg +123456.7-0985432.1+15.9)
```

## Chaining Points Together

Multiple points may be chained by adding each point on a new line followed by the `/` character.

```
ELBIS/
IKUMA/
IDOTO/
GUNAM/
NIKOM/
CIN/
POKOS/
VALRA/
+12.345-098.765/
+15.345-123.765
```

## Airspace.XML Instructions

### SystemRunways

This section 'maps' the runway selectable by the controller in the strip or label of an aircraft to a SID or STAR defined in data for a particular runway (the `DataRunway`). 

For every controlled airport in australia... we need to add the `airport->runways->sidstars`

```xml
<SystemRunways>
	<Airport Name="YBCG">
		<Runway Name="14" DataRunway="14">
			<SID Name="APAGI\d" Type="Jet"/>
			<SID Name="CUDGN\d" />
			<SID Name="CG\d" Default="True" />
			<STAR Name="[A-Z]{4}\dA" ApproachName="ILSZ"/>
			<STAR Name="[A-Z]{4}\dY" ApproachName="RNVY"/>
		</Runway>
		<Runway Name="32" DataRunway="32">
			<SID Name="APAGI\d" Type="Jet"/>
			<SID Name="BURLI\d" />
			<SID Name="CG\d" Default="True" />
			<STAR Name="[A-Z]{4}\dA" ApproachName="RNVZ"/>
			<STAR Name="[A-Z]{4}\dY" ApproachName="RNVY"/>
		</Runway>
		<Runway Name="14V" DataRunway="14">
			<STAR Name="[A-Z]{4}\dV" />
		</Runway>
		<Runway Name="32V" DataRunway="32">
			<STAR Name="[A-Z]{4}\dV" />
		</Runway>
	</Airport>
</SystemRunways>
```

#### What does this all mean?
- The `Name` attribute of `SID` and `STAR` elements accepts Regex search patterns;
- eg. If you see the code `\d` it means any number, so if the APAGI4 becomes APAGI5 the code doesn't need to change.
- eg. `[A-Z]{4}\dA` means the first 4 characters are anything between A-Z, then look for any number then (in this case) Alpha charts. This means the BLAK3A arrival can change to BLAK4A arrival and the code doesn't need to change.
- By doing this `[A-Z]{4}\dA` and `ApproachName="ILSZ"` we have assigned all Alpha STARs the ILSZ approach and `[A-Z]{4}\dY` all Yankee STARs to the `ApproachName="RNVY"` RNAV Yankee approach.
- We set the default SID to the airport's radar departure and we set any visual STAR's under a separate runway called `[runwayid]V` like 14V. We do this by calling all STARs that end in any number and V for Victor/visual using `[A-Z]{4}\dV`.
- The SIDs are written out individually since some are jet and some are non jet.
- **Runway ID cannot be more than 3 characters**, so this means for any parallel runways the visual approach is not a seperate runway entry. Applicable to Sydney and Brisbane (#soon).

### SIDSTARs

This section defines the routes of SIDs, STARs, Approaches and their Transitions.

SIDs and STARs should be defined for controlled airports whenever you wish to remove reliance on Navigraph defined data.

```xml
<SIDSTARs>
	<SID Name="TESTA1" Airport="AAAA" Runways="18,36">
        <Route Runway="36">ROUTE POINT</Route>
        <Route Runway="18">ANTHR RALTO</Route>
        <Route>TESTA</Route>
        <Transition Name="ABCDE">FINSH ABCDE</Transition>
    </SID>
	<STAR Name="TESTA1" Airport="AAAA" Runways="18,36">
		<Transition Name="ABCDE">ABCDE FINSH</Transition>
		<Route>TESTA</Route>
		<Route Runway="36">POINT ROUTE</Route>
		<Route Runway="18">RALTO ANTHR</Route>
	</STAR>
	<Approach Name="RNVZ" Airport="AAAA" Runway="18">
		<Transition Name="ABCDE">ANTHR</Transition>
		<Route>FAFFF AA18T</Route>
	</Approach>
</SIDSTARs>
```

#### What does this all mean?
SIDs and STARs consist of `Route` elements that are runway or non runway specific. For a `SID`, the non-runway specific route will always follow the runway specific route. For a `STAR`, the reverse is true. Transitions will be applied whenever the transition end point coincides with a point on the flight planned route.

Approaches link a STAR to a runway. Transitions will be applied if they conincide with the STAR end point. Approaches are used only if defined in `SystemRunways` and are not manually selectable.

### Airways
Airways may be defined whenever you wish to remove reliance on Navigraph defined data. Airways are always treated as valid in both directions.

```xml
<Airways>
    <Airway Name="A216">
        APUKA/
        MEMIG/
        LOCKA/
        CS
    </Airway>
</Airways>
```

### Intersections

Intersections (Fixes & Navaids) may be defined whenever you wish to remove reliance on Navigraph defined data.

```xml
<Intersections>
    <Point Name="ABARB" Type="Fix">-325106.400+1545604.900</Point>
	<Point Name="WP" Type="Navaid" NavaidType="VOR" Frequency="112.800">-124024.800+1415520.900</Point>
</Intersections>	
```

Duplicates are generally accepted. vatSys will attempt to choose the nearest relevant intersection when parsing to resolve.

#### Intersection Types
```
Types
{
	Fix,
	Navaid,
	Airport,
	Unknown
}
```
#### Navaid Intersection Types
```
NavaidTypes
{
	None,
	VOR,
	NDB,
	TAC
}
```
### Airports

Airports may be defined whenever you wish to remove reliance on Navigraph defined data.

```xml
<Airport ICAO="YABA" Position="-345636.000+1174832.000" Elevation="233">
		<Runway Name="14" Position="-345639.000+1174835.000">
		<Runway Name="32" Position="-345642.000+1174838.000">
</Airport>
```
