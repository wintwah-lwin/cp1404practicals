"""
CP1404/CP5632 - Practical
Broken program to determine score status
"""

score = float(input("Enter score: "))
if score < 0 or score > 100:
    print("Score must be between 0 and 100.")
elif score >= 90:
    print("Excellent")
elif score >= 50:
    print("Pass")
else:
    print("Bad")
