# beauty_parlour.py

customer = input("Enter customer name: ")

service = input("Enter beauty service: ")

service_charge = int(input("Enter service charge: "))

product_charge = int(input("Enter cosmetic product charge: "))

total_bill = service_charge + product_charge

print("Customer Name:", customer)
print("Beauty Service:", service)

print("Service Charge:", service_charge)
print("Product Charge:", product_charge)

print("Total Bill:", total_bill)

if total_bill > 5000:
    print("Premium Beauty Package")
else:
    print("Regular Beauty Service")

appointment = input("Enter appointment date: ")

print("Appointment Date:", appointment)

for i in range(3):
    print("Service Booking Confirmed")

print("Beauty Parlour Management System")
print("Thank You")