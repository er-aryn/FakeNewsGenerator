import random
subjects = [
    "virat kholi",
    "salman bhai",
    "shah ruk khan",
    "manoj master",
    "modi ji",
]
actions = [
    "launches",
    "fights",
    "eats",
    "declear war on",
    "celebrate",
]
places_or_things = [
    "at red fort",
    "in mumbai local",
    "insight parliament",
    "during ipl",
    "school",
]
while True:
    subject = random.choice(subjects)
    action = random.choice(actions)
    places_or_thing = random.choice(places_or_things)

    headline = f"BREAKING NEWS: {subject} {action} {places_or_thing}"
    print("\n" + headline)

    user_input = input("\n DO YOU WANT ANOTHER NEWS? (yes/no)").strip().lower()
    if user_input == "no":
        break

print("\n thanks for using fake news generator")    

