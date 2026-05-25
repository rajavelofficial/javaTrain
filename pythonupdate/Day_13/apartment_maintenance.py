# apartment_maintenance.py

owner = input("Enter owner name: ")

flat_number = input("Enter flat number: ")

maintenance_fee = int(input("Enter maintenance fee: "))

water_charge = int(input("Enter water charge: "))

electricity_charge = int(input("Enter electricity charge: "))

total_bill = maintenance_fee + water_charge + electricity_charge

print("Owner Name:", owner)
print("Flat Number:", flat_number)

print("Maintenance Fee:", maintenance_fee)
print("Water Charge:", water_charge)

print("Electricity Charge:", electricity_charge)
print("Total Bill:", total_bill)

if total_bill > 10000:
    print("High Maintenance Charges")
else:
    print("Normal Charges")

for i in range(3):
    print("Maintenance Bill Generated")

print("Apartment Maintenance System")
print("Thank You")