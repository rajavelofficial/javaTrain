# restaurant_billing.py

customer = input("Enter customer name: ")

food_item = input("Enter food item: ")

quantity = int(input("Enter quantity: "))

price = int(input("Enter item price: "))

total = quantity * price

service_tax = total * 0.08

final_bill = total + service_tax

print("Customer Name:", customer)
print("Food Item:", food_item)

print("Quantity:", quantity)
print("Food Cost:", total)

print("Service Tax:", service_tax)
print("Final Bill:", final_bill)

if final_bill > 3000:
    print("Free Dessert Included")
else:
    print("Normal Billing")

for i in range(3):
    print("Order Served")

print("Restaurant Billing Completed")
print("Visit Again")