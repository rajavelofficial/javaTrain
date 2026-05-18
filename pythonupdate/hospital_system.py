# hospital_system.py

patient = input("Enter patient name: ")

age = int(input("Enter patient age: "))

doctor = input("Enter doctor name: ")

days = int(input("Enter admitted days: "))

room_charge = days * 2000
medicine_charge = 1500

total_bill = room_charge + medicine_charge

print("Patient Name:", patient)
print("Age:", age)
print("Doctor Name:", doctor)

print("Room Charge:", room_charge)
print("Medicine Charge:", medicine_charge)

print("Total Bill:", total_bill)

if total_bill > 10000:
    print("Advance Payment Required")
else:
    print("Normal Payment")

for i in range(3):
    print("Hospital Management System")

print("Thank You")