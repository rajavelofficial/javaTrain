fruits = ("Apple", "Banana", "Mango", "Kiwi", "Strawberry")
#print(fruits)
#print(type(fruits))

fruits += ("Grappes",)
print(fruits)

#Traversal Method-1
for i in range(len(fruits)):
    print(i, fruits[i])

print()
#Traversal Method-2
for i in fruits:
    print(i)

""" 
OUTPUT:
('Apple', 'Banana', 'Mango', 'Kiwi', 'Strawberry', 'Grappes')
0 Apple
1 Banana
2 Mango
3 Kiwi
4 Strawberry
5 Grappes

Apple
Banana
Mango
Kiwi
Strawberry
Grappes
"""