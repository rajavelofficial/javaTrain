# car_rental.py

customer = input("Enter customer name: ")

car = input("Enter car model: ")

days = int(input("Enter rental days: "))

rent_per_day = 3000

total_rent = days * rent_per_day

security_deposit = 5000

final_amount = total_rent + security_deposit

print("Customer Name:", customer)
print("Car Model:", car)

print("Rental Days:", days)
print("Rent Amount:", total_rent)

print("Security Deposit:", security_deposit)
print("Final Amount:", final_amount)

if days >= 7:
    print("Weekly Rental Discount Applied")
else:
    print("Regular Rental")

for i in range(3):
    print("Car Booking Confirmed")

print("Drive Safely")
print("Thank You")