# fish_market.py

customer = input("Enter customer name: ")

fish = input("Enter fish type: ")

weight = int(input("Enter fish weight in kg: "))

price_per_kg = 350

total = weight * price_per_kg

print("Customer Name:", customer)
print("Fish Type:", fish)

print("Fish Weight:", weight)
print("Price Per KG:", price_per_kg)

print("Total Amount:", total)

if total > 5000:
    print("Special Customer Discount")
else:
    print("Regular Billing")

payment = input("Enter payment method: ")

print("Payment Method:", payment)

for i in range(3):
    print("Fish Bill Generated")

print("Fish Market Billing System")
print("Thank You")