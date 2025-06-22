Income = input("Monthly income: ")
Expenses = input("Monthly expenses:" )
savings = float(Income) - float(Expenses)
print("Monthly Savings: " + str(savings))
if savings > 20000:
    print("Great! you are saving well.")
elif savings <5000:
    print("Watch your spending")
