# online_exam.py

student = input("Enter student name: ")

subject = input("Enter subject name: ")

mark = int(input("Enter exam mark: "))

total_mark = 100

percentage = (mark / total_mark) * 100

print("Student Name:", student)
print("Subject:", subject)

print("Exam Mark:", mark)
print("Percentage:", percentage)

if percentage >= 90:
    print("Grade A")
elif percentage >= 75:
    print("Grade B")
elif percentage >= 50:
    print("Grade C")
else:
    print("Fail")

for i in range(3):
    print("Exam Result Published")

print("Online Exam Completed")
print("Thank You")