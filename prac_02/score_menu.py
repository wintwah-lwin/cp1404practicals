"""Score menu prac_02"""

MENU = """
Welcome!
(G)et a valid score
(P)rint result
(S)how stars
(Q)uit
"""

def main():
    #get initial score from user
    user_score = get_valid_score()
    #show menu
    print(MENU)
    choice = input(">>> ").upper()
    while choice != 'Q':
        if choice == 'G':
            #get score
            user_score = get_valid_score()
            print(f"Your score is {user_score}.")
        elif choice == 'P':
            #print result
            user_score = check_if_score_blank(user_score)
            result = get_score_result(user_score)
            print(result)
        elif choice == 'S':
            #print as many stars as score
            user_score = check_if_score_blank(user_score)
            stars = print_symbols(user_score,'*')
            print(stars)
        else:
            print("Invalid choice")
        print(MENU)
        choice = input(">>> ").upper()
    print("Farewell!")

def check_if_score_blank(user_score):
    """ask for score again if score is blank"""
    while user_score == '':
        print('Please enter a score between 0 and 100.')
        user_score = get_valid_score()
    return user_score

def get_valid_score():
    """get a score between 0 and 100 from user"""
    user_score = int(input("Enter score: "))
    while user_score < 0 or user_score > 100:
        print('Score must be between 0 and 100 inclusive.')
        user_score = int(input("Enter score: "))
    return user_score

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

def print_symbols(user_score, symbol='*'):
    """return the number of stars as the score"""
    return f"Your score is {user_score} you get {user_score} stars. \n {symbol * user_score}"

main()
