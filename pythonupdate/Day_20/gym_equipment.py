# gym_equipment.py

equipment = input("Enter equipment name: ")

quantity = int(input("Enter total quantity: "))

available = int(input("Enter available quantity: "))

in_use = quantity - available

maintenance_cost = int(input("Enter maintenance cost: "))

print("Equipment Name:", equipment)
print("Total Quantity:", quantity)

print("Available Quantity:", available)
print("Equipment In Use:", in_use)

print("Maintenance Cost:", maintenance_cost)

if available < 5:
    print("Need Additional Equipment")
else:
    print("Sufficient Equipment Available")

trainer = input("Enter trainer name: ")

print("Trainer Name:", trainer)

for i in range(3):
    print("Equipment Record Updated")

print("Gym Equipment Management System")
print("Thank You")