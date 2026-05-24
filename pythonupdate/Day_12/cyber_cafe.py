# cyber_cafe.py

customer = input("Enter customer name: ")

system_number = int(input("Enter system number: "))

hours = int(input("Enter usage hours: "))

charge_per_hour = 60

total_bill = hours * charge_per_hour

print("Customer Name:", customer)
print("System Number:", system_number)

print("Usage Hours:", hours)
print("Charge Per Hour:", charge_per_hour)

print("Total Bill:", total_bill)

if hours > 5:
    print("Extended Usage")
else:
    print("Normal Usage")

internet_speed = input("Enter internet speed plan: ")

print("Internet Plan:", internet_speed)

for i in range(3):
    print("Session Completed")

print("Cyber Cafe Billing System")
print("Thank You")