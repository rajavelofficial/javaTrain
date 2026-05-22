# hostel_allocation.py

student = input("Enter student name: ")

department = input("Enter department: ")

room_number = int(input("Enter room number: "))

monthly_fee = 4500

months = int(input("Enter number of months: "))

total_fee = monthly_fee * months

print("Student Name:", student)
print("Department:", department)

print("Room Number:", room_number)
print("Monthly Fee:", monthly_fee)

print("Months:", months)
print("Total Hostel Fee:", total_fee)

if total_fee > 20000:
    print("Advance Payment Required")
else:
    print("Regular Payment")

guardian = input("Enter guardian name: ")

print("Guardian Name:", guardian)

for i in range(3):
    print("Room Allocation Successful")

print("Hostel Management Completed")
print("Thank You")