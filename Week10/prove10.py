items = []
prices = []

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
        item_price = float(input(f"What is the price of '{item_name}'? "))
        prices.append(item_price)
        print(f"'{item_name}' has been added to the cart.")
    if action == 2:
        print("The contents of the shopping cart are:")
        for i in range(len(items)):
            print(f'{i + 1}. {items[i]} - ${prices[i]:.2f}')
    if action == 3:
        remove_index = int(input('Which item would you like to remove? ')) - 1
        if remove_index < 0 or remove_index >= len(items):
            print(f'Item number {remove_index + 1} does not exist.')
            continue
        items.pop(remove_index)
        prices.pop(remove_index)
        print('Item removed.')
    if action == 4:
        total = sum(prices)
        print(f"The total price of the items in the shopping cart is ${total:.2f}")
    if action == 5:
        print("Thank you. Goodbye.")
        break
