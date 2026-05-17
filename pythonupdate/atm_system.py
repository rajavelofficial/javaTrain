# atm_system.py

name = input("Enter account holder name: ")

balance = 5000

print("Current Balance:", balance)

withdraw = int(input("Enter withdraw amount: "))

if withdraw <= balance:
    balance = balance - withdraw
    print("Withdrawal Successful")
else:
    print("Insufficient Balance")

print("Available Balance:", balance)

deposit = int(input("Enter deposit amount: "))

balance = balance + deposit

print("Updated Balance:", balance)

for i in range(3):
    print("Bank Transaction Processing")

print("ATM MENU")
print("1. Withdraw")
print("2. Deposit")
print("3. Balance Check")

print("Thank You for Banking")