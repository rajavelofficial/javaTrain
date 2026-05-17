# library_system.py

book_name = input("Enter book name: ")
student_name = input("Enter student name: ")

days = int(input("Enter borrowed days: "))

fine = 0

if days > 7:
    fine = (days - 7) * 10

print("Book Name:", book_name)
print("Student Name:", student_name)
print("Borrowed Days:", days)

if fine > 0:
    print("Fine Amount:", fine)
else:
    print("No Fine")

print("Library Rules")
print("1. Return books on time")
print("2. Keep books safe")
print("3. Maintain silence")

for i in range(3):
    print("Library Management System")

print("Transaction Completed")
print("Thank You")