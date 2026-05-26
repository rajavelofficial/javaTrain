# school_library.py

student = input("Enter student name: ")

book = input("Enter book name: ")

days = int(input("Enter borrowed days: "))

fine = 0

if days > 10:
    fine = (days - 10) * 5

print("Student Name:", student)
print("Book Name:", book)

print("Borrowed Days:", days)
print("Fine Amount:", fine)

author = input("Enter author name: ")

print("Author Name:", author)

category = input("Enter book category: ")

print("Book Category:", category)

for i in range(3):
    print("Library Record Updated")

print("School Library System")
print("Thank You")