# bus_pass.py

student = input("Enter student name: ")

college = input("Enter college name: ")

distance = int(input("Enter travel distance: "))

monthly_fee = distance * 15

print("Student Name:", student)
print("College Name:", college)

print("Travel Distance:", distance)
print("Monthly Fee:", monthly_fee)

if distance > 20:
    print("Long Route Pass")
else:
    print("Short Route Pass")

route = input("Enter bus route number: ")

print("Route Number:", route)

payment = input("Enter payment status: ")

if payment == "paid":
    print("Bus Pass Approved")
else:
    print("Payment Pending")

for i in range(3):
    print("Bus Pass Generated")

print("Student Bus Pass System")
print("Thank You")