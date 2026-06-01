# automobile_showroom.py

customer = input("Enter customer name: ")

vehicle = input("Enter vehicle model: ")

vehicle_price = int(input("Enter vehicle price: "))

insurance = int(input("Enter insurance amount: "))

registration = int(input("Enter registration fee: "))

total_cost = vehicle_price + insurance + registration

print("Customer Name:", customer)
print("Vehicle Model:", vehicle)

print("Vehicle Price:", vehicle_price)
print("Insurance Amount:", insurance)

print("Registration Fee:", registration)
print("Total Cost:", total_cost)

if total_cost > 1000000:
    print("Luxury Vehicle Purchase")
else:
    print("Standard Vehicle Purchase")

for i in range(3):
    print("Purchase Record Updated")

print("Automobile Showroom System")
print("Thank You")