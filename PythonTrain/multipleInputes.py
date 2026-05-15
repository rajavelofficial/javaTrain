import keyword
# Create an empty list to store the inputs
a = []

# Ask the user for how many items they want to input
b = int(input("How many items do you want to enter? "))

# Loop to collect multiple inputs
for i in range(b):
    val = input(f"Enter item {i + 1}: ")
    a.append(val)


for i in a:
    print(i)

print("The list of keywords are : ")
print(keyword.kwlist)