"""
CP1404/CP5632 - Prac 02 - Score
Student Name  - Khant Zay Yar
Student ID    - 14052564
"""


def main():
    score = float(input("Enter score: "))
    print(determine_status(score))


def determine_status(score):
    if score < 0 or score > 100:
        return "Invalid score"
    elif score >= 90:
        return "Excellent"
    elif score >= 50:
        return "Passable"
    else:
        return "Bad"


main()