# pharmacy_billing.py

customer = input("Enter customer name: ")

medicine = input("Enter medicine name: ")

quantity = int(input("Enter quantity: "))

price = int(input("Enter medicine price: "))

total = quantity * price

discount = 0

if total > 3000:
    discount = total * 0.10

final_bill = total - discount

print("Customer Name:", customer)
print("Medicine Name:", medicine)

print("Quantity:", quantity)
print("Total Cost:", total)

print("Discount:", discount)
print("Final Bill:", final_bill)

for i in range(3):
    print("Medicine Bill Generated")

print("Pharmacy Billing System")
print("Thank You")