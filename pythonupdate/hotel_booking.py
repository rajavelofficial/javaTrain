# hotel_booking.py

guest = input("Enter guest name: ")

room_type = input("Enter room type: ")

days = int(input("Enter number of days: "))

room_price = 2500

total = days * room_price

service_charge = 500

final_amount = total + service_charge

print("Guest Name:", guest)
print("Room Type:", room_type)

print("Room Charges:", total)
print("Service Charge:", service_charge)

print("Final Amount:", final_amount)

if final_amount > 10000:
    print("Luxury Booking")
else:
    print("Standard Booking")

for i in range(3):
    print("Room Booking Confirmed")

print("Hotel Management System")
print("Visit Again")

print("Thank You")