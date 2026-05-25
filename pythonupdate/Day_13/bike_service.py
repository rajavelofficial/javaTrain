# bike_service.py

customer = input("Enter customer name: ")

bike = input("Enter bike model: ")

service_charge = int(input("Enter service charge: "))

oil_change = int(input("Enter oil change cost: "))

spare_parts = int(input("Enter spare parts cost: "))

total_bill = service_charge + oil_change + spare_parts

print("Customer Name:", customer)
print("Bike Model:", bike)

print("Service Charge:", service_charge)
print("Oil Change Cost:", oil_change)

print("Spare Parts Cost:", spare_parts)
print("Total Bill:", total_bill)

if total_bill > 8000:
    print("Premium Bike Service")
else:
    print("Standard Bike Service")

for i in range(3):
    print("Bike Service Completed")

print("Bike Ready for Delivery")
print("Thank You")