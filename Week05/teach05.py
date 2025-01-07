grade_percentage = int(input("What is your grade percentage? "))

if grade_percentage >= 90:
    letter_grade = "A"
elif grade_percentage >= 80:
    letter_grade = "B"
elif grade_percentage >= 70:
    letter_grade = "C"
elif grade_percentage >= 60:
    letter_grade = "D"
else:
    letter_grade = "F"

last_digit = grade_percentage % 10

if last_digit >= 7:
    sign = "+"
elif last_digit <= 3:
    sign = "-"
else:
    sign = ""

if grade_percentage >= 93:
    sign = ""
elif letter_grade == "F":
    sign = ""

print(f"Your letter grade is: {letter_grade}{sign}")

if grade_percentage >= 70:
    print("Congratulations, you passed the course!")
else:
    print("I'm sorry, you did not pass the course this time.  Please try again next semester.")
