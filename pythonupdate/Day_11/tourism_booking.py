# tourism_booking.py

customer = input("Enter customer name: ")

place = input("Enter tourist place: ")

days = int(input("Enter number of days: "))

package_cost = int(input("Enter package cost per day: "))

total_cost = days * package_cost

guide_fee = 2000

final_amount = total_cost + guide_fee

print("Customer Name:", customer)
print("Tourist Place:", place)

print("Travel Days:", days)
print("Package Cost:", total_cost)

print("Guide Fee:", guide_fee)
print("Final Amount:", final_amount)

if final_amount > 50000:
    print("Luxury Tour Package")
else:
    print("Standard Tour Package")

for i in range(3):
    print("Tour Booking Confirmed")

print("Happy Journey")
print("Thank You")