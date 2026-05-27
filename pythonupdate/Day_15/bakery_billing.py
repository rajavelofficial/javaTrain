# bakery_billing.py

customer = input("Enter customer name: ")

item = input("Enter bakery item: ")

quantity = int(input("Enter quantity: "))

price = int(input("Enter item price: "))

total = quantity * price

gst = total * 0.05

final_bill = total + gst

print("Customer Name:", customer)
print("Bakery Item:", item)

print("Quantity:", quantity)
print("Item Cost:", total)

print("GST Amount:", gst)
print("Final Bill:", final_bill)

if final_bill > 2000:
    print("Special Discount Applied")
else:
    print("Regular Billing")

for i in range(3):
    print("Order Packed")

print("Bakery Billing Completed")
print("Thank You")