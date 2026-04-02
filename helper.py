#inventory menuimport random


#main menu
#options user has
import random
rank = {
    "you": {'level': 1},
    'enemy': {'level': 10}
}
#global veriables
selfs = {}
cloths = {}
stuff = []
invent = []
skills = []
powers = ["fly", "run", "seek"]
gold = 50
shop = {
    'bodies': {
        'human': {'type': 'form', 'price': 22},
        'bear': {'type': 'form', 'price': 25},
        'goblin': {'type': 'form', 'price': 18},
        'wolf': {'type': 'form', 'price': 22},
    },
    'shirts': {
        'red shirt': {'type': 'shirt', 'price': 20},
        'flag shirt': {'type': 'shirt', 'price': 33},
    },
    'pants': {
        'blue shorts': {'type': 'pants', 'price': 10},
    },
}
body_type = "human"

# Character attributes
# Index: 0 = Strength, 1 = Intelligence, 2 = Speed, 3 = Health
attributes = [10, 8, 6, 100]

# Collected power-ups
powerUps = []

# Souls and Level
souls = 0
level = 1

 
# ATTRIBUTE AND POWER-UP FUNCTIONS
 

#3. Function: Display attributes
#FUNCTION displayAttributes()
#    PRINT "Character Attributes:"
#    PRINT "Strength: " + attributes[0]
#    PRINT "Intelligence: " + attributes[1]
#    PRINT "Health: " + attributes[3]
#END FUNCTION
def displayAttributes():
    print("Character Attributes:")
    print("\nStrength:", attributes[0])
    print("\nIntelligence:", attributes[1])
    print("\nSpeed:", attributes[2])
    print("\nHealth:", attributes[3])

#5. Function: Apply all power-ups to attributes
#FUNCTION applyPowerUps()
#    FOR each powerUp in powerUps
#        SET name = powerUp.name
#        SET statType = powerUp.statType
#        SET amount = powerUp.amount
#
#        IF statType == "strength" THEN
#            attributes[0] = attributes[0] + amount
#        ELSE IF statType == "intelligence" THEN
#            attributes[1] = attributes[1] + amount
#        ELSE IF statType == "speed" THEN
#            attributes[2] = attributes[2] + amount
#        ELSE IF statType == "health" THEN
#            attributes[3] = attributes[3] + amount
#        END IF
#
#        PRINT "Applied " + name + ": " + statType + " +" + amount
#    END FOR
#
#    CLEAR powerUps
#END FUNCTION
def applyPowerUps():
    global powerUps
    for powerUp in powerUps:
        name = powerUp['name']
        statType = powerUp['statType']
        amount = powerUp['amount']

        if statType == "strength":
            attributes[0] += amount
        elif statType == "intelligence":
            attributes[1] += amount
        elif statType == "speed":
            attributes[2] += amount
        elif statType == "health":
            attributes[3] += amount

        print(f"\nApplied {name}: {statType} +{amount}")

    powerUps = []

 
# LEVELING AND SKILL FUNCTIONS
 

# leveling up function
def level_function():
    global level
    #if user has collected 3  of souls then
    if souls >= 3:
        # you have leveled up by one level 1 += level 
        level += 1
        print("you've moved up one level")
    #while level < 10 
    while level < 10:
        # keep adding a level for every three kills
        level += 1

# making a function to view characters options and what skills they have
def characters_options():
    #   storing all the characterics for each character in an induval list
    #   human = {"strength": 23, "health": 50}
    #   dog = {"strength": 47, "health": 120}
    #   goblin = {"strength": 35, "health": 100}
    #   bear = {"strength": 12, "health": 25}
    human = {"strength": 23, "health": 50}
    dog = {"strength": 47, "health": 120}
    goblin = {"strength": 35, "health": 100}
    bear = {"strength": 12, "health": 25}

# making a function to handle skill dependencies and prerequisites(by using if statements)
def skill_change():
    # list for special skills [flying monkey, flying dog,spin kick]
    special_skills = ["flying monkey", "flying dog","spin kick,flying blobfish"]
    # if user had 10 == souls
    if souls == 10: 
        #   show user you have unlocked special skill
        print("\nyou have unlocked a special skills")
        #   pull one of the random skills from the list
        random_skill = random.choice(special_skills)
        #add it onto the skills
        skills.append(random_skill)
    # else if user had eqaul 8 souls
    elif souls == 8:
        #show user you got a special skill
        print("you got a special skills")
        # its flying blobfish 
        print("ITS FLYING BLOBFISH")
        # add blobfish to SKILL LIST
        skills.append("flying blobfish")
    # elif user had 5 == souls
    elif souls == 5:
        #    how user you dont get a skill
        print("you dont get a skill")
    #else print you just moved up a level
    else:
        print("you don't get anything")

 
# SHOP AND INVENTORY FUNCTIONS
 

def get_shop_items():
    #Return a flat list of (name, info, category).
    items = []
    for category, items_dict in shop.items():
        for name, info in items_dict.items():
            items.append((name, info, category))
    return items

def find_in_shop(name):
    #Return (info, category) if name exists in shop, else (None, None)
    for category, items_dict in shop.items():
        if name in items_dict:
            return items_dict[name], category
    return None, None

def shopping():
    global gold, invent, cloths
    #display every item and body in the shop and the price each is at
    print(shop)
    #ask user if they want to buy something
    ask = input("do you want to buy an item? (Y/N)").lower()
    #if ask is yes as y
    if ask == "y":
        #show available items with prices
        print(f"You have {gold} gold.")
        items = get_shop_items()  # returns list of (name, info, category)
        items_map = {}
        for idx, (name, info, category) in enumerate(items, start=1):
            print(f"{idx}. {name} ({category}) - {info.get('price',0)} gold")
            items_map[idx] = (name, info, category)

        choice = input("Enter item number (or press Enter to cancel): ")
        if not choice:
            return
        try:
            num = int(choice)
            if num in items_map:
                name, info, category = items_map[num]
                # proceed to buy/equip: price = info['price']
                price = info['price']
                if gold >= price:
                    gold -= price
                    invent.append(name)
                    if category != "bodies":
                        cloths[name] = info
                    print("You bought", name)
                else:
                    print("Not enough gold.")
            else:
                print("Invalid number.")
        except ValueError:
            print("Please enter a valid number.")

 
def inventory_menu():
    global invent, gold
    while True:
        print("Inventory Menu:")
        print("1. Store Item")
        print("2. Change Item")
        print("3. View Inventory")
        print("4. Quit Inventory")
        choice = input("Choose: ")

        # If user chooses store item
        if choice == "1":
            method = input("collect or buy? ")
            if method == "collect":
                item = input("item name: ")
                invent.append(item)
                print(f"{item} added to inventory")
            elif method == "buy":
                shopping()

        # If user chooses change item
        elif choice == "2":
            print("1. set soul free")
            print("2. use or drop item")
            change = input("choose: ")
            if change == "1":
                souls_in_inventory = [i for i in invent if "soul" in i]
                if souls_in_inventory:
                    print("souls:", souls_in_inventory)
                    soul = input("which soul to free? ")
                    if soul in invent:
                        invent.remove(soul)
                        print("soul freed")
                else:
                    print("no souls in inventory")
            elif change == "2":
                print("inventory:", invent)
                item = input("which item? ")
                if item in invent:
                    action = input("use or drop? ")
                    if action == "use":
                        print("you used", item)
                    elif action == "drop":
                        invent.remove(item)
                        print(item, "dropped")
                else:
                    print("item not found")
        elif choice == "3":
            if not invent:
                print("Your inventory is empty.")
            else:
                for item in invent:
                    print("-", item)
            print(f"Total Gold: {gold}")
        elif choice == "4":
            print("leaving inventory")
            break
        else:
            print("Invalid option")

#run game