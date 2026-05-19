# petrol_bunk.py

customer = input("Enter customer name: ")

fuel_type = input("Enter fuel type: ")

liters = float(input("Enter liters: "))

price_per_liter = 102

total = liters * price_per_liter

print("Customer Name:", customer)
print("Fuel Type:", fuel_type)

print("Liters Filled:", liters)
print("Price Per Liter:", price_per_liter)

print("Total Amount:", total)

if liters >= 20:
    print("Free Car Wash Coupon")
else:
    print("Normal Service")

payment = input("Enter payment method: ")

print("Payment Method:", payment)

for i in range(3):
    print("Billing Completed")

print("Visit Again")
print("Thank You")