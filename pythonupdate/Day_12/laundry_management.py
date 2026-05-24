# laundry_management.py

customer = input("Enter customer name: ")

clothes = int(input("Enter number of clothes: "))

charge_per_cloth = 25

washing_charge = clothes * charge_per_cloth

ironing_charge = 100

final_bill = washing_charge + ironing_charge

print("Customer Name:", customer)
print("Number of Clothes:", clothes)

print("Washing Charge:", washing_charge)
print("Ironing Charge:", ironing_charge)

print("Final Bill:", final_bill)

if clothes > 20:
    print("Bulk Laundry Service")
else:
    print("Regular Laundry Service")

delivery = input("Need home delivery? (yes/no): ")

print("Delivery Option:", delivery)

for i in range(3):
    print("Laundry Process Completed")

print("Laundry Management System")
print("Thank You")