class Bank_Account:
    Customer_Name = ""
    Balance = 0.0
    Account_Number = 0

    def notAvailabe():
        global Account_Number
        print(Account_Number , "is not Available, Please try another account")

cus1 = Bank_Account()
cus1.Customer_Name = "Raja"
cus1.Balance = 100000
cus1.Account_Number = 121701000060

print("Customer Name   : ", cus1.Customer_Name)
print("Account Balance : ", cus1.Balance)
print("Account Number  : ", cus1.Account_Number)