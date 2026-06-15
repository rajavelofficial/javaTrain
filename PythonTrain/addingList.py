#using append values adding single element
num = [1, 2]
num.append(3)
print(num)

num.append(4)
print(num)

#using Insert method add on element as specific posion
mode = [10, 20, 30, 40, 50]
mode.insert(10, 15)
print(mode)

a = [1, 3]
a.insert(1, 2)
print(a)

#Extend method used to update more values
b = [1, 2, 3]
b.extend([4, 5, 6, 7])
print(b)

c = ["SOL", "ETH", "BTC"]
c.extend(["BASE", "BNB", "XRP"])
print(c)
