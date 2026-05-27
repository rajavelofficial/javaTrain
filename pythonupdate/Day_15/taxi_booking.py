# taxi_booking.py

customer = input("Enter customer name: ")

pickup = input("Enter pickup location: ")

destination = input("Enter destination: ")

distance = int(input("Enter travel distance in km: "))

rate_per_km = 18

fare = distance * rate_per_km

print("Customer Name:", customer)
print("Pickup Location:", pickup)

print("Destination:", destination)
print("Travel Distance:", distance)

print("Rate Per KM:", rate_per_km)
print("Total Fare:", fare)

if distance > 50:
    print("Long Distance Trip")
else:
    print("Short Distance Trip")

for i in range(3):
    print("Taxi Booking Confirmed")

print("Taxi Booking System")
print("Thank You")