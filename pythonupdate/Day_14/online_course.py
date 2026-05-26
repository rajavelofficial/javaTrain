# online_course.py

student = input("Enter student name: ")

course = input("Enter course name: ")

duration = int(input("Enter course duration in months: "))

monthly_fee = int(input("Enter monthly fee: "))

total_fee = duration * monthly_fee

print("Student Name:", student)
print("Course Name:", course)

print("Course Duration:", duration)
print("Monthly Fee:", monthly_fee)

print("Total Course Fee:", total_fee)

if total_fee > 20000:
    print("Scholarship Available")
else:
    print("Regular Admission")

mentor = input("Enter mentor name: ")

print("Mentor Name:", mentor)

for i in range(3):
    print("Course Registration Successful")

print("Online Course System")
print("Thank You")