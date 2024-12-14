# Mithril Weather Generator for Traveller RPG

This script generates dynamic and thematic weather for the planet <a href="https://wiki.travellerrpg.com/Mithril_(world)" target="new">Mithril</a> in the Traveller RPG setting. This is based on Mongoose's <a href="https://www.mongoosepublishing.com/products/marches-adventure-2-mission-to-mithril" target="new">Marches Adventure 2: Mission To Mithril</a>. The description of the weather procedure in the module is a little convoluted, but this script attempts to simulate weather conditions based on zones, precipitation patterns, and time since the last storm based on the description. Feel free to use this or modify it as you see fit.

![cold-planet](https://github.com/user-attachments/assets/018f05a0-7996-41e3-a842-b4ba2418abdc)


## Requirements

- **Python Version**: Python 3.8 or higher.

## Usage

1. Clone or download this repository to your local machine.
   - Optionally, you can use an online tool such as https://www.online-python.com/

2. Run the script using a terminal or command prompt:
   ```bash
   python weather.py
   ```
3. Input the required details when prompted:

    - Days since the last storm.
    - Select the zone (Snow Zone, Ice Zone, Arctic Zone).

4. The script will output:

    - A detailed weather description, including temperature and conditions.
    - Precipitation type and intensity (e.g., snow, hail, rain, or storm).

5. Repeat the process as desired for continuous weather updates.

## Example

Here is an example interaction:

```yaml
Days since last storm: 2

Choose a zone
1 : Snow Zone
2 : Ice Zone
3 : Arctic Zone
Zone number (1-3): 1

Weather: Very Cold. -20oC to -40oC. Too cold for much snowfall unless storm.
Precipitation: No precipitation. Overcast or clear sky.
```
