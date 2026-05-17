# calculator.py

num1 = int(input("Enter first number: "))
num2 = int(input("Enter second number: "))

add = num1 + num2
sub = num1 - num2
mul = num1 * num2

print("Addition:", add)
print("Subtraction:", sub)
print("Multiplication:", mul)

if num2 != 0:
    div = num1 / num2
    print("Division:", div)
else:
    print("Division not possible")

print("Calculator Menu")
print("1. Add")
print("2. Subtract")
print("3. Multiply")
print("4. Divide")

for i in range(2):
    print("Calculation Done")

print("Program Finished")