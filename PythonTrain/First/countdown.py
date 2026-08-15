seconds = int(input("Enter countdown time in seconds: "))

delay = 1000
while seconds > 0:
    print("Time left:", seconds)
    seconds -= 1