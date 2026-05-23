# mobile_shop.py

customer = input("Enter customer name: ")

mobile = input("Enter mobile model: ")

price = int(input("Enter mobile price: "))

accessories = int(input("Enter accessories cost: "))

total = price + accessories

gst = total * 0.18

final_amount = total + gst

print("Customer Name:", customer)
print("Mobile Model:", mobile)

print("Mobile Price:", price)
print("Accessories Cost:", accessories)

print("GST Amount:", gst)
print("Final Amount:", final_amount)

if final_amount > 30000:
    print("Premium Customer")
else:
    print("Regular Customer")

for i in range(3):
    print("Billing Successful")

print("Mobile Shop Billing Completed")
print("Thank You")