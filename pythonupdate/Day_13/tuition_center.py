# tuition_center.py

student = input("Enter student name: ")

subject = input("Enter subject name: ")

monthly_fee = int(input("Enter monthly fee: "))

months = int(input("Enter number of months: "))

total_fee = monthly_fee * months

print("Student Name:", student)
print("Subject Name:", subject)

print("Monthly Fee:", monthly_fee)
print("Months:", months)

print("Total Fee:", total_fee)

if total_fee > 10000:
    print("Special Coaching Included")
else:
    print("Regular Coaching")

teacher = input("Enter teacher name: ")

print("Teacher Name:", teacher)

for i in range(3):
    print("Student Record Updated")

print("Tuition Center Management System")
print("Thank You")