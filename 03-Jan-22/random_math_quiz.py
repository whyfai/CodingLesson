
import random

correct_answers = 0

for i in range(10):
    num1 = random.randint(1,10)
    num2 = random.randint(1,10)
    operation = random.choices(["+", "-", "*", "/"])
    operation = operation[0]

    print(num1, operation, num2)
    answer = float(input("Your answer is: "))
    if operation == "+":
        if answer == num1 + num2:
            print("Correct")
            correct_answers += 1
        else:
            print(f"Wrong, the correct answer is {num1+num2}")
    if operation == "-":
        if answer == num1 - num2:
            print("Correct")
            correct_answers += 1
        else:
            print(f"Wrong, the correct answer is {num1-num2}")
    if operation == "*":
        if answer == num1 * num2:
            print("Correct")
            correct_answers += 1
        else:
            print(f"Wrong, the correct answer is {num1*num2}")
    if operation == "/":
        if answer == round(num1 / num2, 2):
            print("Correct")
            correct_answers += 1
        else:
            print(f"Wrong, the correct answer is {round(num1/num2, 2)}")

print(f"Score: {correct_answers*10}%")

"""
Grade chart:
90 - 100 -> A
85 - 89 -> A-
70 - 84 -> B+
65 - 69 -> B
60 - 64 -> B-
55 - 59 -> C
<55 -> D
"""

def get_grade(score):
    if score >= 90:
        return "A"
    elif score >= 85:
        return "A-"
    elif score >= 70:
        return "B+"
    elif score >= 65:
        return "B"
    elif score >= 60:
        return "B-"
    elif score >= 55:
        return "C"
    else:
        return "D"

print("Grade:", get_grade(correct_answers*10))