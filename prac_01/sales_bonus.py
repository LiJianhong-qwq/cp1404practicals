"""
Program to calculate and display a user's bonus based on sales.
If sales are under $1,000, the user gets a 10% bonus.
If sales are $1,000 or over, the bonus is 15%.
"""
sales = float(input("Enter sales: $"))
if sales < 1000:
    cost = sales * (1 - 0.1)
    print(f"You will get {sales - cost}$ bonus.")
    print(f"Cost: {cost}")
if sales >= 1000:
    cost = sales * (1 - 0.15)
    print(f"You will get {sales - cost}$ bonus.")
    print(f"Cost: {cost}")






