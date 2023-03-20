"""
CP1404/CP5632 - Practical
Broken program to determine score status
"""
import random


def main():
    score = float(input("Enter score: "))
    print(calculate_result(score))
    number = export_result()
    print(f"Random score: {number}")
    print(calculate_result(number))


def calculate_result(score):
    if score < 0:
        return "Invalid score"
    elif score > 100:
        return "Invalid score"
    elif score > 90:
        return "Excellent"
    elif score > 50:
        return "Passable"
    else:
        return "Bad"


def export_result():
    number = random.randint(0, 100)
    return number


main()


