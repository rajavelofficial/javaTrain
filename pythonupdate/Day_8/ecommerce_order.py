# ecommerce_order.py

customer = input("Enter customer name: ")

product = input("Enter product name: ")

quantity = int(input("Enter quantity: "))

price = int(input("Enter product price: "))

total = quantity * price

shipping_charge = 100

final_amount = total + shipping_charge

print("Customer Name:", customer)
print("Product Name:", product)

print("Quantity:", quantity)
print("Product Cost:", total)

print("Shipping Charge:", shipping_charge)
print("Final Amount:", final_amount)

if final_amount > 5000:
    print("Free Gift Added")
else:
    print("Regular Order")

for i in range(3):
    print("Order Packed")

print("E-Commerce Order Completed")
print("Thank You")