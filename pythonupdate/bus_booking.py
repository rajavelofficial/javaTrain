# bus_booking.py

name = input("Enter passenger name: ")

source = input("Enter source place: ")
destination = input("Enter destination place: ")

tickets = int(input("Enter number of tickets: "))

ticket_price = 750

total = tickets * ticket_price

print("Passenger Name:", name)
print("Source:", source)
print("Destination:", destination)

print("Ticket Price:", ticket_price)
print("Total Amount:", total)

if tickets >= 5:
    print("Group Booking Applied")
else:
    print("Normal Booking")

for i in range(3):
    print("Booking Confirmed")

print("Bus Ticket Menu")
print("1. Book Ticket")
print("2. Cancel Ticket")
print("3. Ticket Status")

print("Thank You for Booking")