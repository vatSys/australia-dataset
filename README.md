# Eurocat Australia Dataset
This is the default profile dataset for vatSys.

## Aeronautical Information Management
The Australian vatSys dataset is maintained by the [VATPAC AIS Team](https://vatpac.org/about/staff) to support virtual air traffic operations within the YMMM and YBBB FIRs.

The team regularly updates the dataset through scheduled AIRAC updates aligned with the [Airservices Document Amendment Calendar](https://www.airservicesaustralia.com/industry-info/aeronautical-information-management/document-amendment-calendar/), with interim AIRAC updates released as required.

### Community Contributions
#### AIRAC Data
The majority of files in the dataset are prepared using automated tools and internal VATPAC processes which overwrite manual changes each update. For this reason, most AIRAC files can not be directly edited by members outside of the AIS team. If you notice an error, or have a suggestion for a change, please let us know by [raising an issue via GitHub](https://github.com/vatSys/australia-dataset/issues) or logging a ticket via the [VATPAC Helpdesk](https://helpdesk.vatpac.org).

#### Custom Map Layers
For a map to be considered for inclusion into the Australia or Pacific profile:
- It must be compatible with the AIS AIRAC maintenance process.
  - ie, it can't need any Airspace.xml or TCU.xml changes
- It must not duplicate, or make redundant, any existing AIS map layer;
- It must be reasonably expected to be useful to the provision of ATS within VATPAC airspace;
- It must be designed to replicate operations as they are simulated online - not necessarily as they exist in the real world;
- It must be available for use by all appropriately credentialled VATPAC members, and not for exclusive use by members of any third-party organisation or group;
- It must not contain any personal information not relevant to the functionality of the map;
- It should use a colour/design scheme that will not be confused with an existing AIS map layer;
- It must be approved by both the AIS Manager and ATS Director.

If you are considering contributing a map layer and are unsure how these requirements would apply, please reach out to the AIS team directly by raising an [issue](https://github.com/vatSys/australia-dataset/issues) before commencing work on the change.

#### Plugins
The Australia dataset contains plugins from trusted partners that have been reviewed and endorsed by the VATPAC Air Traffic Services and Technology teams.

Plugins are assessed on a case-by-case basis for quality, utility, alignment with VATPAC strategic objectives, and long-term sustainability.

Developers interested in integrating a plugin to the profile are invited contact the Air Traffic Services team via the [VATPAC Helpdesk](https://helpdesk.vatpac.org) _before_ commencing development. Unsolicited contributions of completed plugins are **strongly discouraged**.