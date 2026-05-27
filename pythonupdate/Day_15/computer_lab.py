# computer_lab.py

student = input("Enter student name: ")

lab_number = int(input("Enter lab number: "))

system_number = int(input("Enter system number: "))

hours = int(input("Enter usage hours: "))

lab_fee = hours * 40

print("Student Name:", student)
print("Lab Number:", lab_number)

print("System Number:", system_number)
print("Usage Hours:", hours)

print("Lab Fee:", lab_fee)

if hours > 4:
    print("Extended Lab Usage")
else:
    print("Regular Lab Usage")

faculty = input("Enter faculty name: ")

print("Faculty Name:", faculty)

for i in range(3):
    print("Lab Record Updated")

print("Computer Lab Management System")
print("Thank You")