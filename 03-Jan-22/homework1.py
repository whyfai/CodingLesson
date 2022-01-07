"""
Zhang San’s username is an extra-legal fanatic, and his password is 12138. 
Please design a program to determine whether the entered username and password are correct. 
To prevent brute force cracking, there are only 3 input opportunities. 
If more than 3 times, the program will report an error.
"""

username = "an extra-legal fanatic"
password = "12138"

inputs = 0

while inputs < 3:
    username_input = input("Username: ")
    password_input = input("Password: ")
    if username_input == username and password_input == password:
        print("Welcome Zhang San!")
        break
    else:
        print("Wrong username and/or password.")
        inputs += 1
        if inputs == 3:
            print("Too many failed attempts. You have been locked out.")
            break