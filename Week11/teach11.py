with open('hr_system.txt') as file:
    for line in file:
        fields = line.split()
        name = fields[0]
        id = fields[1]
        title = fields[2]
        salary = fields[3]
        monthly_pay = float(salary) / 24
        if title == 'Engineer':
            monthly_pay += 1000
        print(f'{name} (ID: {id}), {title} - ${monthly_pay:.2f}')
