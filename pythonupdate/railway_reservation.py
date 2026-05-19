# railway_reservation.py

passenger = input("Enter passenger name: ")

train = input("Enter train name: ")

seats = int(input("Enter number of seats: "))

ticket_price = 850

total = seats * ticket_price

print("Passenger Name:", passenger)
print("Train Name:", train)

print("Seats Booked:", seats)
print("Ticket Price:", ticket_price)

print("Total Fare:", total)

if seats > 5:
    print("Bulk Booking Applied")
else:
    print("Regular Booking")

status = input("Enter payment status: ")

if status == "paid":
    print("Ticket Confirmed")
else:
    print("Payment Pending")

for i in range(3):
    print("Reservation Processing")

print("Thank You for Using Railway Service")