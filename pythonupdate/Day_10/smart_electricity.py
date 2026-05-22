# smart_electricity.py

consumer = input("Enter consumer name: ")

previous_reading = int(input("Enter previous reading: "))

current_reading = int(input("Enter current reading: "))

units = current_reading - previous_reading

rate = 9

bill_amount = units * rate

print("Consumer Name:", consumer)
print("Previous Reading:", previous_reading)

print("Current Reading:", current_reading)
print("Units Consumed:", units)

print("Rate Per Unit:", rate)
print("Bill Amount:", bill_amount)

if units > 500:
    print("High Power Consumption")
else:
    print("Normal Usage")

for i in range(3):
    print("Electricity Bill Processed")

print("Smart Electricity System")
print("Thank You")