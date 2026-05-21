# school_fee.py

student = input("Enter student name: ")

standard = input("Enter class: ")

tuition_fee = int(input("Enter tuition fee: "))

bus_fee = int(input("Enter bus fee: "))

exam_fee = int(input("Enter exam fee: "))

total_fee = tuition_fee + bus_fee + exam_fee

print("Student Name:", student)
print("Class:", standard)

print("Tuition Fee:", tuition_fee)
print("Bus Fee:", bus_fee)

print("Exam Fee:", exam_fee)
print("Total Fee:", total_fee)

if total_fee > 50000:
    print("Installment Facility Available")
else:
    print("Full Payment Required")

for i in range(3):
    print("Fee Receipt Generated")

print("School Fee Management Completed")
print("Thank You")