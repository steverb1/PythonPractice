maximum = -1
maximum_county = ''

state_of_interest = input('Which state are you interested in? ')

with open('states_counties.txt') as file:
    data = file.readlines()
    for line in data:
        line = line.strip().split(':')
        county = line[0]
        quantity = int(line[1])
        state = line[2]

        if state == state_of_interest:
            print(f'State: {state}, County: {county}, Quantity: {quantity}')
            if quantity > maximum:
                maximum = quantity
                maximum_county = county
    
print(f'The county with the most courthouses is: {maximum_county}')
print(f'It has {maximum} courthouses.')
