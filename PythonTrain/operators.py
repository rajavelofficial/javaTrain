a = 12
b = 21
c = 12

print(a > b)
print(a < b)
print(a == b)

food = []
while True:
    f = input("What food do you like? : ")
    if f == "quit":
        break
    food.append(f)

    """
    O/P:
    
False
True
False
What food do you like? : apple
What food do you like? : Banana
What food do you like? : Mango
What food do you like? : quit

    """