# mobile_repair.py

customer = input("Enter customer name: ")

mobile = input("Enter mobile model: ")

problem = input("Enter mobile problem: ")

service_charge = int(input("Enter service charge: "))

parts_cost = int(input("Enter spare parts cost: "))

total_bill = service_charge + parts_cost

print("Customer Name:", customer)
print("Mobile Model:", mobile)

print("Problem:", problem)
print("Service Charge:", service_charge)

print("Parts Cost:", parts_cost)
print("Total Bill:", total_bill)

if total_bill > 5000:
    print("Major Repair Service")
else:
    print("Minor Repair Service")

for i in range(3):
    print("Repair Process Completed")

print("Mobile Ready for Delivery")
print("Thank You")