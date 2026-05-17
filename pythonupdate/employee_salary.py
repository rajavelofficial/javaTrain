# employee_salary.py

name = input("Enter employee name: ")
basic = int(input("Enter basic salary: "))

hra = basic * 0.20
da = basic * 0.10
bonus = 2000

total_salary = basic + hra + da + bonus

print("Employee Name:", name)
print("Basic Salary:", basic)
print("HRA:", hra)
print("DA:", da)
print("Bonus:", bonus)

print("Total Salary:", total_salary)

if total_salary > 50000:
    print("High Salary Employee")
else:
    print("Normal Salary Employee")

for i in range(3):
    print("Salary Processed")

print("Thank You")