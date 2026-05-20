# pharmacy_system.py

customer = input("Enter customer name: ")

medicine = input("Enter medicine name: ")

quantity = int(input("Enter quantity: "))

price = int(input("Enter medicine price: "))

total = quantity * price

gst = total * 0.05

final_amount = total + gst

print("Customer Name:", customer)
print("Medicine Name:", medicine)

print("Quantity:", quantity)
print("Medicine Cost:", total)

print("GST Amount:", gst)
print("Final Amount:", final_amount)

if final_amount > 2000:
    print("Health Discount Applied")
else:
    print("Regular Billing")

for i in range(3):
    print("Medicine Packed")

print("Pharmacy Billing Completed")
print("Thank You")