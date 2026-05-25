# water_tank_monitor.py

building = input("Enter building name: ")

capacity = int(input("Enter tank capacity in liters: "))

current_level = int(input("Enter current water level: "))

used_water = capacity - current_level

print("Building Name:", building)
print("Tank Capacity:", capacity)

print("Current Water Level:", current_level)
print("Used Water:", used_water)

if current_level < 500:
    print("Low Water Level Alert")
else:
    print("Water Level Normal")

motor = input("Motor status (on/off): ")

print("Motor Status:", motor)

for i in range(3):
    print("Water Tank Status Updated")

print("Water Tank Monitoring System")
print("Thank You")