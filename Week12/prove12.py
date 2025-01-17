countries = []
years = []
expectancies = []

sum_for_year = 0
count_for_year = 0
max_for_year = 0
min_for_year = 999
max_country = ''
min_country = ''

year_of_interest = int(input('Enter the year of interest: '))
print()

with open('life-expectancy.csv') as file:
    data = file.readlines()
    first_line = True
    for line in data:
        if first_line:
            first_line = False
            continue
        line = line.split(',')
        country = line[0]
        year = int(line[2])
        expectancy = float(line[3])

        countries.append(country)
        years.append(year)
        expectancies.append(expectancy)

        if year == year_of_interest:
            sum_for_year += expectancy
            if expectancy > max_for_year:
                max_for_year = expectancy
                max_country = country
            if expectancy < min_for_year:
                min_for_year = expectancy
                min_country = country
            count_for_year += 1

max_life_expectancy = max(expectancies)
max_index = expectancies.index(max_life_expectancy)
print('The overall max life expectancy is:', max_life_expectancy, 'from', countries[max_index], 'in', years[max_index])

min_life_expectancy = min(expectancies)
min_index = expectancies.index(min_life_expectancy)
print('The overall min life expectancy is:', min_life_expectancy, 'from', countries[min_index], 'in', years[min_index])
print()

print(f'For the year {year_of_interest}:')
print(f'The average life expectancy across all countries was {sum_for_year / count_for_year:.2f}')
print(f'The max life expectancy was in {max_country} with {max_for_year}')
print(f'The min life expectancy was in {min_country} with {min_for_year}')
