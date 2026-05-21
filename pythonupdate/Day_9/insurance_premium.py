# insurance_premium.py

customer = input("Enter customer name: ")

policy = input("Enter policy type: ")

age = int(input("Enter customer age: "))

premium = int(input("Enter yearly premium: "))

years = int(input("Enter policy years: "))

total_amount = premium * years

print("Customer Name:", customer)
print("Policy Type:", policy)

print("Customer Age:", age)
print("Yearly Premium:", premium)

print("Policy Years:", years)
print("Total Amount:", total_amount)

if age > 60:
    print("Senior Citizen Policy")
else:
    print("Regular Policy")

for i in range(3):
    print("Policy Processing")

print("Insurance Premium System")
print("Thank You")