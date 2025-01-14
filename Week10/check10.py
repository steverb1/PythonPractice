item = ''
shopping_list = []

print('Please enter the items of the shopping (type: quit to finish:')

while item != 'quit':
    item = input('Item: ')
    if item != 'quit':
        shopping_list.append(item)

print('The shopping list is:')
for item in shopping_list:
    print(item)

print()

print('The shopping list with indexes is:')
for i in range(len(shopping_list)):
    print(f'{i}. {shopping_list[i]}')

print()
item_index_to_change = int(input('Which item would you like to change? '))
new_item = input('What is the new item? ')

shopping_list[item_index_to_change] = new_item

print()
print('The shopping list with indexes is:')
for i in range(len(shopping_list)):
    print(f'{i}. {shopping_list[i]}')
