# laptop_service.py

customer = input("Enter customer name: ")

laptop = input("Enter laptop model: ")

service_type = input("Enter service type: ")

service_charge = int(input("Enter service charge: "))

parts_cost = int(input("Enter parts replacement cost: "))

total_bill = service_charge + parts_cost

print("Customer Name:", customer)
print("Laptop Model:", laptop)

print("Service Type:", service_type)
print("Service Charge:", service_charge)

print("Parts Cost:", parts_cost)
print("Total Bill:", total_bill)

if total_bill > 15000:
    print("Advanced Repair Service")
else:
    print("Basic Repair Service")

for i in range(3):
    print("Laptop Service Completed")

print("Laptop Ready for Delivery")
print("Thank You")