# fitness_tracker.py

user = input("Enter user name: ")

steps = int(input("Enter steps walked: "))

calories = int(input("Enter calories burned: "))

water = int(input("Enter water intake in liters: "))

print("User Name:", user)
print("Steps Walked:", steps)

print("Calories Burned:", calories)
print("Water Intake:", water)

if steps >= 10000:
    print("Daily Goal Achieved")
else:
    print("Need More Exercise")

bmi = float(input("Enter BMI value: "))

print("BMI Value:", bmi)

for i in range(3):
    print("Fitness Data Updated")

print("Fitness Tracker System")
print("Stay Healthy")