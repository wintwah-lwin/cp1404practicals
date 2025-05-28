"""
CP1404/CP5632 - Practical
Program to determine score status
"""
import random

def main():
    #get user score and print result
    score = float(input("Enter score: "))
    result = get_score_result(score)
    print(f"Your score is {result}.")

    #get random score and print result
    random_score = random.randint(1, 100)
    random_score_result = get_score_result(random_score)
    print(f"The random score is {random_score} and the result is {random_score_result}.")

def get_score_result(score):
    """determine score result"""
    if score < 0 or score > 100:
        return "Score must be between 0 and 100."
    elif score >= 90:
        return "Excellent"
    elif score >= 50:
        return "Pass"
    else:
        return "Bad"


main()