name = input("What is your name? ")
income = input("Monthly income: Rs. ")
expenses = input("Monthly expenses: Rs. ")
savings = float(income) - float(expenses)
saving_percentage = round((float(savings) / float(income) * 100),1)
if saving_percentage >= 35:
    print(name + ", you are saving " + str(saving_percentage) + "%. Great job.")
elif saving_percentage <= 5:
    print(name + ",savings are just " + str(saving_percentage) + "%. Let's plan better.")
else:
    print(name + "you are saving " + str(saving_percentage) + "%. That's OK.")
