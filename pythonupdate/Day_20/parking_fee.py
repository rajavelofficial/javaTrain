# parking_fee.py

owner = input("Enter vehicle owner name: ")

vehicle_number = input("Enter vehicle number: ")

vehicle_type = input("Enter vehicle type: ")

hours = int(input("Enter parking hours: "))

fee_per_hour = 30

parking_fee = hours * fee_per_hour

print("Owner Name:", owner)
print("Vehicle Number:", vehicle_number)

print("Vehicle Type:", vehicle_type)
print("Parking Hours:", hours)

print("Fee Per Hour:", fee_per_hour)
print("Parking Fee:", parking_fee)

if parking_fee > 500:
    print("Long Duration Parking")
else:
    print("Short Duration Parking")

payment_status = input("Enter payment status: ")

print("Payment Status:", payment_status)

for i in range(3):
    print("Parking Receipt Generated")

print("Parking Fee Collection System")
print("Thank You")