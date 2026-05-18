# electricity_bill.py

customer = input("Enter customer name: ")

units = int(input("Enter electricity units: "))

rate = 8

bill = units * rate

tax = bill * 0.05

final_bill = bill + tax

print("Customer Name:", customer)
print("Units Consumed:", units)

print("Current Bill:", bill)
print("Tax Amount:", tax)

print("Final Bill:", final_bill)

if final_bill > 5000:
    print("High Electricity Usage")
else:
    print("Normal Electricity Usage")

for i in range(3):
    print("Bill Generated Successfully")

print("Electricity Board")
print("Payment Due Date: 25th")

print("Thank You")