"""
In Python, whether the variable name is legal is very important. 
Please design a program to judge whether the input variable name is legal. 

Variable name requirements: 
Variable names can be composed of letters, numbers or underscores, 
and variable names can only start with letters or underscores.
"""

alphabet = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
numbers = ['1','2','3','4','5','6','7','8','9','0']

input = input("Enter a variable name: ")

invalid_name = False

if input[0] in alphabet or input[0] == "_":
    for i in input:
        if i[0] in alphabet or i[0] in numbers or i[0] == "_":
            continue
        else:
            print("That is a illegal variable name in Python!")
            invalid_name = True
            break
else:
    print("That is a illegal variable name in Python!")
    invalid_name = True

if not invalid_name:
    print("That is a legal variable name in Python!")