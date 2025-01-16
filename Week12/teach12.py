counties = []
quantities = []
states = []

with open('states_counties.txt') as file:
    data = file.readlines()
    for line in data:
        line = line.strip().split(':')
        counties.append(line[0])
        quantities.append(int(line[1]))
        states.append(line[2])

        print(f'State: {line[2]}, County: {line[0]}, Quantity: {line[1]}')
    
maximium = max(quantities)
print(f'The county with the most courthouses is: {counties[quantities.index(maximium)]}')
print(f'It has {maximium} courthouses.')
