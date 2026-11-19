def area_of_rectangle(Length, width):
    return Length*width

Length = int(input("Enter the Area Length : "))
width = int(input("Enter the Area width : "))

TotalAreaOfRectangle = area_of_rectangle(Length, width)
print(TotalAreaOfRectangle)