# water_bill.py

customer = input("Enter customer name: ")

units = int(input("Enter water units used: "))

rate_per_unit = 12

bill = units * rate_per_unit

service_charge = 100

final_bill = bill + service_charge

print("Customer Name:", customer)
print("Water Units:", units)

print("Water Bill:", bill)
print("Service Charge:", service_charge)

print("Final Bill:", final_bill)

if final_bill > 3000:
    print("High Water Consumption")
else:
    print("Normal Water Usage")

payment = input("Enter payment status: ")

if payment == "paid":
    print("Payment Successful")
else:
    print("Payment Pending")

for i in range(3):
    print("Water Bill Generated")

print("Thank You")