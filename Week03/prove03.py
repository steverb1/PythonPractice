child_meal_price = float(input("What is the price of a child's meal? "))
adult_meal_price = float(input("What is the price of an adult's meal? "))
number_of_children = int(input('How many children are there? '))
number_of_adults = int(input('How many adults are there? '))
sales_tax_rate = float(input('What is the sales tax rate? '))

subtotal = child_meal_price * number_of_children + adult_meal_price * number_of_adults
print(f'Subtotal: ${subtotal}')
