# flight_reservation.py

passenger = input("Enter passenger name: ")

flight = input("Enter flight name: ")

tickets = int(input("Enter number of tickets: "))

ticket_price = 4500

total_fare = tickets * ticket_price

print("Passenger Name:", passenger)
print("Flight Name:", flight)

print("Tickets Booked:", tickets)
print("Ticket Price:", ticket_price)

print("Total Fare:", total_fare)

if tickets >= 3:
    print("Travel Discount Applied")
else:
    print("Standard Fare")

seat = input("Enter seat type: ")

print("Seat Type:", seat)

for i in range(3):
    print("Flight Ticket Confirmed")

print("Happy Journey")
print("Thank You")