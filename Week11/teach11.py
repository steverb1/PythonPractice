with open('hr_system.txt') as file:
    for line in file:
        line = line.split()
        print(f'Name: {line[0]}, Title: {line[2]}')
