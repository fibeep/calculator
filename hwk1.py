salary = int(input("How much money do you make?"))
spending = int (input("How much do you spend per month?"))
saving = salary - spending

if spending >= salary * 0.9:
    print("You are spending too much money")
else:
    print("Good job, you are on the path to financial freedom")

print("You are currently saving " + str(saving) + " dollars per month")

future = int(input("How much money do you want to have in your savings in 10 years? (Please include only a number)"))

if future / 10 <= salary:
    print("You need to save",future/10,"dollars every year from now on.")
else:
    print("You need to find a new job that pays" + str(future/10) + "because with your current salary it is impossible to save this much money")