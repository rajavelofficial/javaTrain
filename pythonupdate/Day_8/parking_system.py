# parking_system.py

owner = input("Enter vehicle owner name: ")

vehicle = input("Enter vehicle type: ")

hours = int(input("Enter parking hours: "))

charge_per_hour = 40

total_charge = hours * charge_per_hour

print("Owner Name:", owner)
print("Vehicle Type:", vehicle)

print("Parking Hours:", hours)
print("Charge Per Hour:", charge_per_hour)

print("Total Parking Charge:", total_charge)

if hours > 5:
    print("Long Time Parking")
else:
    print("Normal Parking")

slot = input("Enter parking slot number: ")

print("Allocated Slot:", slot)

for i in range(3):
    print("Parking Ticket Generated")

print("Parking System Completed")
print("Thank You")