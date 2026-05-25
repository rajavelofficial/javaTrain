# grocery_store.py

customer = input("Enter customer name: ")

item = input("Enter grocery item: ")

quantity = int(input("Enter quantity: "))

price = int(input("Enter item price: "))

total = quantity * price

packing_charge = 50

final_bill = total + packing_charge

print("Customer Name:", customer)
print("Grocery Item:", item)

print("Quantity:", quantity)
print("Item Cost:", total)

print("Packing Charge:", packing_charge)
print("Final Bill:", final_bill)

if final_bill > 4000:
    print("Discount Coupon Added")
else:
    print("Regular Purchase")

for i in range(3):
    print("Billing Completed")

print("Grocery Store System")
print("Thank You")