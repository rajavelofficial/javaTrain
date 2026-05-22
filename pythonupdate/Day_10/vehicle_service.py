# vehicle_service.py

customer = input("Enter customer name: ")

vehicle = input("Enter vehicle model: ")

service_type = input("Enter service type: ")

service_charge = int(input("Enter service charge: "))

parts_charge = int(input("Enter spare parts charge: "))

total_bill = service_charge + parts_charge

print("Customer Name:", customer)
print("Vehicle Model:", vehicle)

print("Service Type:", service_type)
print("Service Charge:", service_charge)

print("Parts Charge:", parts_charge)
print("Total Bill:", total_bill)

if total_bill > 10000:
    print("Premium Service")
else:
    print("Regular Service")

for i in range(3):
    print("Vehicle Service Completed")

print("Vehicle Ready for Delivery")
print("Thank You")