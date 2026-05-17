# number_check.py

num = int(input("Enter a number: "))

if num > 0:
    print("Positive Number")
elif num < 0:
    print("Negative Number")
else:
    print("Zero")

if num % 2 == 0:
    print("Even Number")
else:
    print("Odd Number")

square = num * num
cube = num * num * num

print("Square:", square)
print("Cube:", cube)

for i in range(5):
    print("Checking Number")

print("Program Ended")
print("Execution Successful")