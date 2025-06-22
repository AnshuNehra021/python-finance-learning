Income = input("Monthly income: Rs. ")
Expenses = input("Monthly expenses: Rs. " )
savings = float(Income) - float(Expenses)
print("Monthly Savings: Rs. " + str(round(savings,0)))
if savings > 20000:
    print("Great! you are saving well.")
elif savings <5000:
    print("Watch your spending.")
else:
    print("You are doing well.")
