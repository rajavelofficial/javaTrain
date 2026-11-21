class Bank_Account:
    def __init__(self, Customer_Name, Balance, Account_Number):
        self.Customer_Name = Customer_Name
        self.Balance = Balance
        self.Account_Number = Account_Number

    def __del__(self):
        pass

    def notAvailabe():
        global Account_Number
        print(Account_Number , "is not Available, Please try another account")

cus1 = Bank_Account(Customer_Name = "Raja", Balance = 100000, Account_Number = 121701000060)

cus2 = Bank_Account("Arun", 500, 284983848)

print("Customer Name   : ", cus1.Customer_Name)
print("Account Balance : ", cus1.Balance)
print("Account Number  : ", cus1.Account_Number,"\n")

print("Customer Name   : ", cus2.Customer_Name)
print("Account Balance : ", cus2.Balance)
print("Account Number  : ", cus2.Account_Number, "\n")