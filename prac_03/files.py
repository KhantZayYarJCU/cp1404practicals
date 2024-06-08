"""
CP1404/CP5632 - Prac 03 - Files
Student Name  - Khant Zay Yar
Student ID    - 14052564
"""

# Question 1
name = input("Enter your name: ")
with open('name.txt', 'w') as file:
    file.write(name)

# Question 2
with open('name.txt', 'r') as file:
    name = file.read().strip()
    print(f"Hi {name}!")

# Question 3
with open('numbers.txt', 'r') as file:
    number1 = int(file.readline())
    number2 = int(file.readline())
    total = number1 + number2
    print("Total of first two numbers:", total)

# Question 4
total = 0
with open('numbers.txt', 'r') as file:
    for line in file:
        total += int(line)
print("Total of all numbers:", total)