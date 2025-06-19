import random

MIN_NUMBER = 1
MAX_NUMBER = 45
NUMBER_PER_LINE = 6

number_of_pick = int(input("How many quick picks? : "))
for i in range(number_of_pick):
    quick_picks = []
    while len(quick_picks) < NUMBER_PER_LINE:
        number = random.randint(MIN_NUMBER, MAX_NUMBER)
        if number not in quick_picks:
            quick_picks.append(number)
    quick_picks.sort()
    print(" ".join(f"{n:2}" for n in quick_picks))
