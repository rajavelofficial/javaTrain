# library_stock.py

book = input("Enter book name: ")

author = input("Enter author name: ")

stock = int(input("Enter available stock: "))

issued = int(input("Enter issued books count: "))

remaining = stock - issued

print("Book Name:", book)
print("Author Name:", author)

print("Available Stock:", stock)
print("Issued Books:", issued)

print("Remaining Books:", remaining)

if remaining < 5:
    print("Need to Add More Books")
else:
    print("Stock Available")

category = input("Enter book category: ")

print("Category:", category)

for i in range(3):
    print("Library Stock Updated")

print("Library System Completed")
print("Thank You")