countries = []
years = []
expectancies = []

with open('life-expectancy.csv') as file:
    data = file.readlines()
    first_line = True
    for line in data:
        if first_line:
            first_line = False
            continue
        line = line.split(',')
        countries.append(line[0])
        years.append(int(line[2]))
        expectancies.append(float(line[3]))

print('The overall max life expectancy is:', max(expectancies))
print('The overall min life expectancy is:', min(expectancies))
