# crop_management.py

farmer = input("Enter farmer name: ")

crop = input("Enter crop name: ")

land = int(input("Enter land area in acres: "))

yield_per_acre = int(input("Enter yield per acre: "))

total_yield = land * yield_per_acre

print("Farmer Name:", farmer)
print("Crop Name:", crop)

print("Land Area:", land)
print("Yield Per Acre:", yield_per_acre)

print("Total Yield:", total_yield)

if total_yield > 1000:
    print("High Production")
else:
    print("Normal Production")

season = input("Enter crop season: ")

print("Season:", season)

for i in range(3):
    print("Crop Data Updated")

print("Agriculture Management Completed")
print("Thank You")