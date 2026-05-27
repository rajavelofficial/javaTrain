# dairy_farm.py

farmer = input("Enter farmer name: ")

cows = int(input("Enter number of cows: "))

milk_per_cow = int(input("Enter milk per cow in liters: "))

total_milk = cows * milk_per_cow

price_per_liter = 45

income = total_milk * price_per_liter

print("Farmer Name:", farmer)
print("Number of Cows:", cows)

print("Milk Per Cow:", milk_per_cow)
print("Total Milk:", total_milk)

print("Price Per Liter:", price_per_liter)
print("Total Income:", income)

if income > 50000:
    print("High Production Farm")
else:
    print("Normal Production Farm")

for i in range(3):
    print("Dairy Record Updated")

print("Dairy Farm Management System")
print("Thank You")