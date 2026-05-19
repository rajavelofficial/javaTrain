# gym_membership.py

member = input("Enter member name: ")

age = int(input("Enter age: "))

plan = input("Enter membership plan: ")

monthly_fee = 1500

months = int(input("Enter number of months: "))

total = monthly_fee * months

print("Member Name:", member)
print("Age:", age)

print("Membership Plan:", plan)
print("Monthly Fee:", monthly_fee)

print("Total Amount:", total)

if months >= 12:
    print("Free Personal Training Added")
else:
    print("Standard Membership")

trainer = input("Need trainer? (yes/no): ")

if trainer == "yes":
    print("Trainer Assigned")
else:
    print("No Trainer Selected")

for i in range(3):
    print("Membership Activated")

print("Welcome to the Gym")