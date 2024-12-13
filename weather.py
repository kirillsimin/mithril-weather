import random, sys

ZONES = ["Snow Zone", "Ice Zone", "Arctic Zone"]
ZONE_MODIFIERS = [0, -2, -4]
WEATHER_CONDITIONS = [
    "Extremely Cold. -50oC and below. Snowfall unlikely. Strong winds common with small ice particles.",
    "Very Cold. -20oC to -40oC. Too cold for much snowfall unless storm.",
    "Cold. -10oC.  Snowfall or hail is common, and can last for several hours.",
    "Cool. 0-4oC. An Ephemeral Glade is possible in areas with thin snow cover. Snowfall or hail likely but intermittent",
    "Warm. 4-8oC, rarely 10oC. Melting of thinner ice. Ephemeral Glade is likely. Some rain or sleet likely."
]

def roll_2d6():
    return random.randint(1, 6) + random.randint(1, 6)

def get_conditions(days_since_storm, zone_id):
    roll = roll_2d6()
    
    # Snow zone, ignore all DMs
    if zone_id == 0:
        return roll
    
    # add zone and storm modifiers
    dm = -4 if days_since_storm == 1 else 0
    dm = dm + ZONE_MODIFIERS[zone_id]
    return roll + dm

def get_condition_category(condition_roll):
    if condition_roll <= 2:
        return 0
    elif 3 <= condition_roll <= 5:
        return 1
    elif 6 <= condition_roll <= 9:
        return 2
    elif 10 <= condition_roll <= 11:
        return 3
    else:
        return 4

def get_percipitation(days_since_storm, large_change_yesterday):
    if large_change_yesterday and (roll_2d6() >= 8):
        return 13 # storm
    
    return roll_2d6() + days_since_storm  

def get_percipitation_description(percipitation, weather_condition):
    if percipitation < 7:
        return "No percipitation. Overcast or clear sky."

    if percipitation >= 13:
        lightning = random.randint(1, 6) == 6
        length = roll_2d6()
        description = "Storm " + str(length) + " hours! Strong gusty winds that blow snow into deep drifts, \
driving hail or snow, and heavy precipitation. Visibility reduced to almost nothing. "
        
        description = description + "\nRepeated spectacular lightning strikes!" if lightning else description
        
        return description

    if weather_condition <= 9:
        return random.choice(["Snow.", "Hail."])
    elif 10 <= weather_condition <= 11:
        return random.choice(["Sleet.", "Hail."])
    else:
        return "Rain."

def get_days_since():
    try:
        days = input("Days since last storm: ")
        print(days)
        return int(days)
    except:
        return 0

def get_large_change(condition_categories):
        if len(condition_categories) >= 3:
            large_change = condition_categories[-2] - condition_categories[-3] >= 2
        else:
            large_change = False
        
        return large_change

def get_zone():
    try:
        print("\nChoose a zone")
        for (i,k) in enumerate(ZONES):
            print(i + 1, ": ", k)
        zone = input("Zone number (1-" + str(len(ZONES)) + "): ")
        return int(zone) - 1
    except KeyboardInterrupt:
        print("\n\nSafe Travels!")
        sys.exit()
    except:
        return 0

if __name__ == "__main__":
    days_since_storm = get_days_since()

    condition_categories = []
    percipitations = []

    while(True):
        zone_id = get_zone()
        
        conditions = get_conditions(days_since_storm, zone_id)
        condition_categories.append(get_condition_category(conditions))

        large_change = get_large_change(condition_categories)

        percipitations.append(get_percipitation(days_since_storm, large_change))

        print("\n")
        print(WEATHER_CONDITIONS[condition_categories[-1]])
        print(get_percipitation_description(percipitations[-1], condition_categories[-1]))
        print("\n")
        
        days_since_storm = 0 if percipitations[-1] >= 13 else days_since_storm + 1
