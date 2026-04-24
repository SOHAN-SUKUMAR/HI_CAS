inventory = {}
consumption = {}

def add_item():
    item = input("Enter item name: ")
    quantity = int(input("Enter quantity: "))
    threshold = int(input("Enter threshold level: "))

    inventory[item] = {"quantity": quantity, "threshold": threshold}
    consumption[item] = []

    print("Item added successfully.")

def use_item():
    item = input("Enter item name: ")

    if item not in inventory:
        print("Item not found.")
        return

    qty = int(input("Enter quantity used: "))

    if qty > inventory[item]["quantity"]:
        print("Not enough stock.")
        return

    inventory[item]["quantity"] -= qty
    consumption[item].append(qty)

    print("Usage recorded.")


def check_low_stock():
    for item in inventory:
        if inventory[item]["quantity"] <= inventory[item]["threshold"]:
            print("Low stock alert for:", item)


def predict_runout():
    item = input("Enter item name: ")

    if item not in inventory:
        print("Item not found.")
        return

    if len(consumption[item]) == 0:
        print("No consumption data available.")
        return

    total = 0
    for qty in consumption[item]:
        total += qty

    average_use = total / len(consumption[item])

    if average_use == 0:
        print("No usage detected.")
        return

    days_left = inventory[item]["quantity"] / average_use

    print(item, "will approximately run out in", int(days_left), "usage cycles.")

def analytics_report():
    print("\n--- Consumption Report ---")
    for item in consumption:
        total = 0
        for qty in consumption[item]:
            total += qty
        print(item, "Total Used:", total)

while True:
    print("\n--- HI-CAS MENU ---")
    print("1. Add Item")
    print("2. Use Item")
    print("3. Check Low Stock")
    print("4. Predict Runout")
    print("5. Analytics Report")
    print("6. Exit")

    choice = input("Enter choice: ")

    if choice == "1":
        add_item()
    elif choice == "2":
        use_item()
    elif choice == "3":
        check_low_stock()
    elif choice == "4":
        predict_runout()
    elif choice == "5":
        analytics_report()
    elif choice == "6":
        print("Exiting HI-CAS...")
        break
    else:
        print("Invalid choice.")