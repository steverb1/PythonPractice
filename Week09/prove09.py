items = []

print("Welcome to the Shopping Cart Program!")

while True:
    print()
    print("Please select one of the following:")
    print("1. Add item")
    print("2. View cart")
    print("3. Remove item")
    print("4. Compute total")
    print("5. Quit")

    action = int(input("Please enter an action: "))

    if action == 1:
        item_name = input("What item would you like to add? ")
        items.append(item_name)
        print(f"'{item_name}' has been added to the cart.")
    elif action == 2:
        print("The contents of the shopping cart are:")
        for item in items:
            print(item)
    elif action == 5:
        print("Thank you. Goodbye.")
        break
