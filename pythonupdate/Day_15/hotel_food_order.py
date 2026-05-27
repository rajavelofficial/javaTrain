# hotel_food_order.py

customer = input("Enter customer name: ")

food = input("Enter food item: ")

quantity = int(input("Enter quantity: "))

price = int(input("Enter food price: "))

total = quantity * price

service_charge = 100

final_bill = total + service_charge

print("Customer Name:", customer)
print("Food Item:", food)

print("Quantity:", quantity)
print("Food Cost:", total)

print("Service Charge:", service_charge)
print("Final Bill:", final_bill)

if final_bill > 2500:
    print("Complimentary Drink Added")
else:
    print("Regular Order")

for i in range(3):
    print("Food Order Confirmed")

print("Hotel Food Ordering System")
print("Thank You")