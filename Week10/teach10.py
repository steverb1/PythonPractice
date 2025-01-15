print('Enter the names and balances of bank accounts (type: quit when done)')

account_names = []
account_balances = []

name = ''

while name != 'quit':
    name = input('What is the name of the account? ')
    if name != 'quit':
        balance = float(input('What is the balance? '))
        account_names.append(name)
        account_balances.append(balance)

print()
print('Account Information:')
for i in range(len(account_names)):
    print(f'{i}. {account_names[i]} - ${account_balances[i]:.2f}')

print()
print(f'Total: ${sum(account_balances):.2f}')
print(f'Average: ${sum(account_balances) / len(account_balances):.2f}')

highest_index = account_balances.index(max(account_balances))
print(f'Highest balance: {account_names[highest_index]} - ${account_balances[highest_index]:.2f}')

update = True
while update:
    print()
    update = input('Would you like to update an account? ') == 'yes'
    if update:
        index = int(input('Which account do you want to update? '))
        account_balances[index] = float(input('What is the new amount? '))

    print()
    print('Account Information:')
    for i in range(len(account_names)):
        print(f'{i}. {account_names[i]} - ${account_balances[i]:.2f}')
