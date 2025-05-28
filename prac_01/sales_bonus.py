"""
Program to calculate and display a user's bonus based on sales.
If sales are under $1,000, the user gets a 10% bonus.
If sales are $1,000 or over, the bonus is 15%.
"""

MENU = """Enter sales to calculate bonus.
Enter a negative number to quit."""
print(MENU)
sales = float(input("Enter sales: $"))
while sales >=0:
    if sales < 1000:
        bonus = sales * 0.1
        print(f"You get ${bonus:.2f} bonus.")
    elif sales >= 1000:
        bonus = sales * 0.15
        print(f"You get ${bonus:.2f} bonus.")
    else:
        print("Invalid amount.")
    print(MENU)
    sales = float(input("Enter sales: $"))
print("Program stopped. Thank you.")
