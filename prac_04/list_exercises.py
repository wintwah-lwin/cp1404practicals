"""Basic list operations"""
NUMBER_OF_INPUTS = 5
numbers = []
while len(numbers) < NUMBER_OF_INPUTS:
    number = int(input("Enter a number: "))
    numbers.append(number)

print(f"The first number is: {numbers[0]}")
print(f"The last number is {numbers[-1]}")
print(f"The smallest number is: {min(numbers)}")
print(f"The largest number is: {max(numbers)}")
print(f"The average number is: {sum(numbers)/len(numbers):.1f}")

"""Woefully inadequate security checker"""
usernames = ['jimbo', 'giltson98', 'derekf', 'WhatSup', 'NicolEye', 'swei45', 'BaseInterpreterInterface', 'BaseStdIn',
             'Command', 'ExecState', 'InteractiveConsole', 'InterpreterInterface', 'StartServer', 'bob']
username = input("Enter your username: ")
if username in usernames:
    print("Access granted")
else:
    print("Access denied")