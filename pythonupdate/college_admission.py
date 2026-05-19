# college_admission.py

student = input("Enter student name: ")

department = input("Enter department name: ")

cutoff = float(input("Enter cutoff mark: "))

fees = 50000

print("Student Name:", student)
print("Department:", department)

print("Cutoff Mark:", cutoff)
print("Course Fees:", fees)

if cutoff >= 180:
    print("Admission Approved")
else:
    print("Admission Waiting List")

hostel = input("Need hostel? (yes/no): ")

if hostel == "yes":
    print("Hostel Facility Added")
else:
    print("Hostel Not Required")

for i in range(3):
    print("Admission Processing")

print("College Admission Completed")
print("Thank You")