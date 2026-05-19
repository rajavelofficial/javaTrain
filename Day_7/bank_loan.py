# bank_loan.py

customer = input("Enter customer name: ")

loan_amount = int(input("Enter loan amount: "))

interest_rate = 8

years = int(input("Enter loan years: "))

interest = (loan_amount * interest_rate * years) / 100

total_payment = loan_amount + interest

print("Customer Name:", customer)
print("Loan Amount:", loan_amount)

print("Interest Rate:", interest_rate)
print("Loan Period:", years)

print("Interest Amount:", interest)
print("Total Payment:", total_payment)

if loan_amount > 500000:
    print("Loan Requires Manager Approval")
else:
    print("Loan Approved")

for i in range(3):
    print("Loan Processing")

print("Bank Loan System")
print("Thank You")