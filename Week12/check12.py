people = [
    "Stephanie 36",
    "John 29",
    "Emily 24",
    "Gretchen 54",
    "Noah 12",
    "Penelope 32",
    "Michael 2",
    "Jacob 10"
]

names = []
ages = []

for person in people:
    person = person.split()
    names.append(person[0])
    ages.append(int(person[1]))

minimum_age = min(ages)
print('The youngest person is', names[ages.index(minimum_age)], 'who is', minimum_age, 'years old.')
