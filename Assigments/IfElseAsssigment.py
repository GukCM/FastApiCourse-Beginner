# - Create a variable grade holding an integer between 0 - 100
# - Code if, elif, else statements to print the letter grade of the number grade variable
# Grades:
# A = 90 - 100
# B = 80 - 89
# C = 70-79
# D = 60 - 69
# F = 0 - 59

# Example:
# if grade = 87 then print('B')

grade = 15

if grade > 89 and grade < 101:
    print("A")

elif grade > 79 and grade < 90:
    print("B")

elif grade > 69 and grade < 80:
    print("C")

elif grade > 59 and grade < 70:
    print("D")

elif grade >=0 and grade < 60:
    print("F")

else:
    print("Incorrect")

