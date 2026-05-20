# attendance_system.py

student = input("Enter student name: ")

total_days = int(input("Enter total working days: "))

present_days = int(input("Enter present days: "))

attendance = (present_days / total_days) * 100

print("Student Name:", student)
print("Total Working Days:", total_days)

print("Present Days:", present_days)
print("Attendance Percentage:", attendance)

if attendance >= 75:
    print("Eligible for Exam")
else:
    print("Not Eligible for Exam")

department = input("Enter department name: ")

print("Department:", department)

for i in range(3):
    print("Attendance Record Updated")

print("Attendance Management System")
print("Thank You")