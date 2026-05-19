# courier_tracking.py

customer = input("Enter customer name: ")

tracking_id = input("Enter tracking ID: ")

weight = int(input("Enter parcel weight: "))

charge = weight * 50

print("Customer Name:", customer)
print("Tracking ID:", tracking_id)

print("Parcel Weight:", weight)
print("Courier Charge:", charge)

status = input("Enter delivery status: ")

if status == "delivered":
    print("Courier Delivered Successfully")
else:
    print("Courier In Transit")

location = input("Enter current location: ")

print("Current Location:", location)

for i in range(3):
    print("Tracking Updated")

print("Courier Service System")
print("Thank You")