# mobile_recharge.py

customer = input("Enter customer name: ")

mobile = input("Enter mobile number: ")

plan = int(input("Enter recharge amount: "))

validity = 28

print("Customer Name:", customer)
print("Mobile Number:", mobile)

print("Recharge Amount:", plan)
print("Plan Validity:", validity, "Days")

if plan >= 499:
    print("Unlimited Data Activated")
else:
    print("Basic Plan Activated")

gst = plan * 0.18

final_amount = plan + gst

print("GST Amount:", gst)
print("Total Amount:", final_amount)

for i in range(3):
    print("Recharge Successful")

print("Recharge Completed")
print("Thank You")