# Simple Inventory System
inventory = {}

def add_item():
    name = input("Enter item name: ").lower()
    quantity = int(input("Enter quantity: "))

    if name in inventory:
        inventory[name] += quantity
        print(f"Updated! New quantity of '{name}' is {inventory[name]}")
    else:
        inventory[name] = quantity
        print(f"Item '{name}' added with quantity {quantity}")

def get_item():
    name = input("Enter item name to search: ").lower()

    if name in inventory:
        print(f"Item: {name}")
        print(f"Quantity: {inventory[name]}")
    else:
        print("Item not found in inventory.")

def total_quantity():
    total = sum(inventory.values())
    print(f"Total quantity of all items: {total}")

def display_inventory():
    if not inventory:
        print("Inventory is empty.")
    else:
        print("\nCurrent Inventory:")
        for item, qty in inventory.items():
            print(f"{item} : {qty}")
while True:
    print("\n--- Inventory Menu ---")
    print("1. Add/Update Item")
    print("2. Retrieve Item Information")
    print("3. Display Total Quantity")
    print("4. Display Full Inventory")
    print("5. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        add_item()
    elif choice == "2":
        get_item()
    elif choice == "3":
        total_quantity()
    elif choice == "4":
        display_inventory()
    elif choice == "5":
        print("Exiting program...")
        break
    else:
        print("Invalid choice. Please try again.")
