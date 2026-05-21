# event_management.py

organizer = input("Enter organizer name: ")

event = input("Enter event name: ")

participants = int(input("Enter number of participants: "))

fee = int(input("Enter registration fee: "))

total_collection = participants * fee

print("Organizer Name:", organizer)
print("Event Name:", event)

print("Participants:", participants)
print("Registration Fee:", fee)

print("Total Collection:", total_collection)

if participants >= 100:
    print("Large Scale Event")
else:
    print("Small Scale Event")

venue = input("Enter venue name: ")

print("Venue:", venue)

for i in range(3):
    print("Event Registration Successful")

print("Event Management Completed")
print("Thank You")