# crop_management.py

farmer = input("Enter farmer name: ")

crop = input("Enter crop name: ")

land_area = int(input("Enter land area in acres: "))

seed_cost = int(input("Enter seed cost: "))

fertilizer_cost = int(input("Enter fertilizer cost: "))

total_expense = seed_cost + fertilizer_cost

print("Farmer Name:", farmer)
print("Crop Name:", crop)

print("Land Area:", land_area)
print("Seed Cost:", seed_cost)

print("Fertilizer Cost:", fertilizer_cost)
print("Total Expense:", total_expense)

if land_area > 10:
    print("Large Scale Farming")
else:
    print("Small Scale Farming")

season = input("Enter farming season: ")

print("Season:", season)

for i in range(3):
    print("Crop Details Updated")

print("Crop Management System")
print("Thank You")