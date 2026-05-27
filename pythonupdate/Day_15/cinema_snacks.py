# cinema_snacks.py

customer = input("Enter customer name: ")

snack = input("Enter snack item: ")

quantity = int(input("Enter quantity: "))

price = int(input("Enter snack price: "))

total = quantity * price

gst = total * 0.05

final_bill = total + gst

print("Customer Name:", customer)
print("Snack Item:", snack)

print("Quantity:", quantity)
print("Snack Cost:", total)

print("GST Amount:", gst)
print("Final Bill:", final_bill)

if final_bill > 1000:
    print("Combo Offer Applied")
else:
    print("Regular Purchase")

for i in range(3):
    print("Snack Bill Generated")

print("Cinema Snack Counter System")
print("Thank You")