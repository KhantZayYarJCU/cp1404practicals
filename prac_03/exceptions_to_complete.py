"""
CP1404/CP5632 - Practical
Fill in the TODOs to complete the task
"""

is_finished = False
while not is_finished:
    try:
        result = int(input("Enter a valid integer: "))
        # TODO: Add the specific exception you want to catch after except
    except ValueError:  # Catching ValueError if input cannot be converted to an integer
        print("Please enter a valid integer.")
    else:
        is_finished = True  # Set is_finished to True if a valid integer is entered

print("Valid result is:", result)