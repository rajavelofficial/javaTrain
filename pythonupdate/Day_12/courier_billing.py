# courier_billing.py

customer = input("Enter customer name: ")

parcel_type = input("Enter parcel type: ")

weight = int(input("Enter parcel weight: "))

charge_per_kg = 80

delivery_charge = weight * charge_per_kg

print("Customer Name:", customer)
print("Parcel Type:", parcel_type)

print("Parcel Weight:", weight)
print("Charge Per KG:", charge_per_kg)

print("Delivery Charge:", delivery_charge)

if weight > 10:
    print("Heavy Parcel Service")
else:
    print("Standard Parcel Service")

destination = input("Enter destination city: ")

print("Destination:", destination)

for i in range(3):
    print("Courier Bill Generated")

print("Courier Billing System")
print("Thank You")