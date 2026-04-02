from helper import displayAttributes, applyPowerUps,  inventory_menu, shopping,skill_change,powerUps
 
# MAIN MENU + INVENTORY MENU
 

def main_menu():
    while True:
        print("1. View Attributes")
        print("2. Add Power-Up")
        print("3. Use Power-Ups")
        print("4. Inventory Menu")
        print("5. Shop")
        print("6. Skill Check")
        print("7. Exit")
        choice = input("Choose: ")

        if choice == "1":
            displayAttributes()
        elif choice == "2":
            name = input("Power-Up Name: ")
            statType = input("Stat Type (strength/intelligence/speed/health): ")
            amount = int(input("Amount: "))
            powerUps.append({"name": name, "statType": statType, "amount": amount})
        elif choice == "3":
            applyPowerUps()
        elif choice == "4":
            inventory_menu()
        elif choice == "5":
            shopping()
        elif choice == "6":
            skill_change()
        elif choice == "7":
            print("Exiting game...")
            break


main_menu()