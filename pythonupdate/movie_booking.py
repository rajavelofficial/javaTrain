# movie_booking.py

customer = input("Enter customer name: ")

movie = input("Enter movie name: ")

tickets = int(input("Enter number of tickets: "))

ticket_price = 200

total = tickets * ticket_price

print("Customer Name:", customer)
print("Movie Name:", movie)

print("Ticket Price:", ticket_price)
print("Total Amount:", total)

if tickets >= 4:
    discount = total * 0.10
    print("Discount:", discount)
    total = total - discount
else:
    print("No Discount")

print("Final Amount:", total)

for i in range(3):
    print("Ticket Booking Confirmed")

print("Enjoy Your Movie")
print("Thank You")