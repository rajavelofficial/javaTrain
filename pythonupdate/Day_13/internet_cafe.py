# internet_cafe.py

customer = input("Enter customer name: ")

computer = int(input("Enter computer number: "))

hours = int(input("Enter usage hours: "))

rate = 70

total_bill = hours * rate

print("Customer Name:", customer)
print("Computer Number:", computer)

print("Usage Hours:", hours)
print("Rate Per Hour:", rate)

print("Total Bill:", total_bill)

if hours >= 6:
    print("Discount Eligible")
else:
    print("Regular Charges")

service = input("Need printing service? (yes/no): ")

print("Printing Service:", service)

for i in range(3):
    print("Session Recorded")

print("Internet Cafe Billing Completed")
print("Thank You")