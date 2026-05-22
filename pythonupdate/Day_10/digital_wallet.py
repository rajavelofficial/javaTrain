# digital_wallet.py

user = input("Enter user name: ")

mobile = input("Enter mobile number: ")

balance = 3000

print("Available Balance:", balance)

recharge = int(input("Enter recharge amount: "))

balance = balance + recharge

print("Updated Balance:", balance)

payment = int(input("Enter payment amount: "))

if payment <= balance:
    balance = balance - payment
    print("Payment Successful")
else:
    print("Insufficient Balance")

print("Remaining Balance:", balance)

for i in range(3):
    print("Transaction Completed")

print("Digital Wallet System")
print("Thank You")