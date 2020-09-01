salary = int(input("How much money do you make?"))
spending = int (input("How much do you spend per month?"))
saving = salary - spending

if spending >= salary * 0.9:
    print("You are spending too much money")
else:
    print("Good job, you are on the path to financial freedom")

