income = float(input("Monthly income: "))
expenses = float(input("Monthly expenses: "))
def calculation_saving (income, expenses):
     return income - expenses
saving = calculation_saving(income, expenses)
print(f"Monthly saving: {saving}")
def saving_percentage (saving, income):
    return round(saving / income * 100,1)
saving_percentage = saving_percentage (saving, income)
if saving_percentage > 35:
    print("Well done! Great savings")
elif saving_percentage > 10:
    print("You are doing well")
else:
    print("Check your expenses")
