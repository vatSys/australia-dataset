# vatsys-australia-dataset
Default profile dataset for vatSys

Profile.xml must be updated each release

## Airspace.XML Instructions

For every controlled airport in australia... we need to add the `airport->runways->sidstars`

```xml
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
```
### What does this all mean?
- If you see the code `\d` it means any number, so if the APAGI4 becomes APAGI5 the code doesn't need to change.
- `[A-Z]{4}\dA` means the first 4 characters are anything between A-Z, then look for any number then (in this case) Alpha charts. This means the BLAK3A arrival can change to BLAK4A arrival and the code doesn't need to change.
- By doing this `[A-Z]{4}\dA` and `ApproachName="ILSZ"` we have assigned all Alpha STARs the ILSZ approach and `[A-Z]{4}\dY` all Yankee STARs to the `ApproachName="RNVY"` RNAV Yankee approach.
- We set the default star to the airport's radar departure and we set any visual STAR's under a separate runway called `[runwayid]V` like 14V. We do this by calling all STARs that end in any number and V for Victor/visual using `[A-Z]{4}\dV`.
- The SIDs are written out individually since some are jet and some are non jet.
- **Runway ID cannot be more than 3 characters**, so this means for any parallel runways the visual approach is not a seperate runway entry. Applicable to Sydney and Brisbane (#soon).
