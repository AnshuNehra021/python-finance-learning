#task 1:
expenses = [25000, 27000, 22000, 30000, 28000, 26000]
for x in expenses:
    print("Expenses: " + str(x))

total = float(sum(expenses))
average = float(round((total/len(expenses)),2))

print(f"Total expenses: {total}")
print(f"Average: {average}")

for x in expenses:
    if x > 27000:
        print(f"Higher monthly expenses: {x}")

#task 2:
expenses1 = []
for i in range(5):
    amount = float(input(f"Write expense amount {i+1}: "))
    expenses1.append(amount)
print(expenses1)
print(f"Max expenses: {max(expenses1)}")
print(f"Min expenses: {min(expenses1)}")
