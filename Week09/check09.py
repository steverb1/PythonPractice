friends = []

new_friend = ''

while new_friend != 'end':
    new_friend = input('Type the name of a friend: ')
    if new_friend != 'end':
        friends.append(new_friend)

if len(friends) > 0:
    print('Your friends are:')
    for friend in friends:
        print(friend)
