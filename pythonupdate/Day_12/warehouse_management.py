# warehouse_management.py

manager = input("Enter manager name: ")

product = input("Enter product name: ")

stock_in = int(input("Enter stock received: "))

stock_out = int(input("Enter stock dispatched: "))

available_stock = stock_in - stock_out

print("Manager Name:", manager)
print("Product Name:", product)

print("Stock Received:", stock_in)
print("Stock Dispatched:", stock_out)

print("Available Stock:", available_stock)

if available_stock < 20:
    print("Low Warehouse Stock")
else:
    print("Stock Level Normal")

location = input("Enter warehouse location: ")

print("Warehouse Location:", location)

for i in range(3):
    print("Warehouse Record Updated")

print("Warehouse Management Completed")
print("Thank You")