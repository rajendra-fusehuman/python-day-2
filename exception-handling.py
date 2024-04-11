'''Write a Python program that takes two integers as input and performs division
 (num1 / num2). Handle the ZeroDivisionError and display a custom error message
 when the second number is zero
'''
def divide_numbers(num1, num2):
    try:
        result = num1 / num2
        print("Result of division:", result)
    except ZeroDivisionError:
        print("Error!! Division by zero is not allowed!")

num1 = 50
num2 = 5
divide_numbers(num1, num2)


'''Implement a program that takes user input for a filename, opens the file in read mode,
 and displays its contents. Handle the FileNotFoundError and display an error message
  if the file is not found
'''
def display_file_contents(filename):
    try:
        with open(filename, 'r') as file:
            for line in file:
                print(line, end='')
    except FileNotFoundError:
        print("Error: File not found.")

# def main():
#     filename = input("Enter the filename: ")
#     display_file_contents(filename)


'''Write a Python program that takes a user input and converts it to an integer.
 Handle the ValueError and display a custom error message when the input cannot be
  converted to an integer
'''
def convert_to_integer(user_input):
    try:
        num = float(user_input)
        num = int(num)
        print("Converted integer:", num)
    except ValueError:
        print("Error!! cannot convert to an integer.")

def main():
    user_input = input("Enter a number: ")
    convert_to_integer(user_input)


'''Write a Python program that takes two integers as input and performs division
(num1 / num2). Handle both ValueError (if non-integer input) and ZeroDivisionError
and display appropriate error messages.
'''
def divide_numbers(num1, num2):
    try:
        result = num1 / num2
        print("Result of division:", result)
    except ZeroDivisionError:
        print("Error: Division by zero is not allowed!")

def main():
    try:
        num1 = int(input("Enter the first number: "))
        num2 = int(input("Enter the second number: "))
        divide_numbers(num1, num2)
    except ValueError:
        print("Error: Please enter valid integers.")


'''Write a Python program that takes user input for age. Create a custom exception
 InvalidAgeError to handle cases where the age is below 0 or above 120
'''
class InvalidAgeError(Exception):
    pass

def check_age(age):
    if age < 0 or age > 120:
        raise InvalidAgeError("Age must be between 0 and 120.")

def main():
    age = int(input("Enter your age: "))
    check_age(age)
    print("Your age is:", age)


'''Implement a program that reads user input for a password. Create a custom exception
 WeakPasswordError to handle cases where the password is shorter than 8 characters
'''
class WeakPasswordError(Exception):
    pass

def check_password(password):
    if len(password) < 8:
        raise WeakPasswordError("Password is shorter than 8 characters.")
    else:
        print(f"password: {password}")

def main():
    password = input("Enter your password: ")
    check_password(password)
