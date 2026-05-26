# bus_transport.py

driver = input("Enter driver name: ")

bus_number = input("Enter bus number: ")

route = input("Enter bus route: ")

passengers = int(input("Enter passenger count: "))

ticket_rate = 25

collection = passengers * ticket_rate

print("Driver Name:", driver)
print("Bus Number:", bus_number)

print("Bus Route:", route)
print("Passenger Count:", passengers)

print("Ticket Rate:", ticket_rate)
print("Total Collection:", collection)

if passengers > 40:
    print("Bus Fully Occupied")
else:
    print("Seats Available")

for i in range(3):
    print("Transport Data Updated")

print("Bus Transport Management System")
print("Thank You")