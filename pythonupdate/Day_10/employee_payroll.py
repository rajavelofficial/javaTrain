# employee_payroll.py

employee = input("Enter employee name: ")

basic_salary = int(input("Enter basic salary: "))

hra = basic_salary * 0.20

da = basic_salary * 0.10

pf = basic_salary * 0.05

net_salary = basic_salary + hra + da - pf

print("Employee Name:", employee)
print("Basic Salary:", basic_salary)

print("HRA:", hra)
print("DA:", da)

print("PF Deduction:", pf)
print("Net Salary:", net_salary)

if net_salary > 60000:
    print("Senior Employee")
else:
    print("Junior Employee")

for i in range(3):
    print("Payroll Generated")

print("Employee Payroll Completed")
print("Thank You")