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
    print(f'{account_names[i]} - ${account_balances[i]:.2f}')

print(f'Total: ${sum(account_balances):.2f}')
print(f'Average: ${sum(account_balances) / len(account_balances):.2f}')
