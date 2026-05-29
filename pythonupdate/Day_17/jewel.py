# jewelry_shop.py

customer = input("Enter customer name: ")

jewel = input("Enter jewelry type: ")

weight = float(input("Enter jewelry weight in grams: "))

price_per_gram = 6500

making_charge = 2000

gold_price = weight * price_per_gram

final_bill = gold_price + making_charge

print("Customer Name:", customer)
print("Jewelry Type:", jewel)

print("Gold Weight:", weight)
print("Gold Price:", gold_price)

print("Making Charge:", making_charge)
print("Final Bill:", final_bill)

if final_bill > 100000:
    print("Premium Gold Customer")
else:
    print("Regular Customer")

for i in range(3):
    print("Jewelry Bill Generated")

print("Jewelry Shop Billing System")
print("Thank You")