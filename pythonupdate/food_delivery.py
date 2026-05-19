# food_delivery.py

customer = input("Enter customer name: ")

food = input("Enter food item: ")

quantity = int(input("Enter quantity: "))

price = 250

total = quantity * price

delivery_charge = 50

final_amount = total + delivery_charge

print("Customer Name:", customer)
print("Food Item:", food)

print("Quantity:", quantity)
print("Food Cost:", total)

print("Delivery Charge:", delivery_charge)
print("Final Amount:", final_amount)

if final_amount > 1000:
    print("Free Dessert Added")
else:
    print("Normal Order")

for i in range(3):
    print("Order Preparing")

print("Food Delivery Successful")
print("Thank You")