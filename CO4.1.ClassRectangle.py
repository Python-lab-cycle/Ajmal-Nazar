class rectangle:
    def area(l,b):
        area1=l*b
        return area1
    def perimeter(l,b):
        peri=2*(l+b)
        return peri
l1=int(input("Enter length of first rectangle:"))
b1=int(input("Enter breadth of first rectangle:"))
l2=int(input("Enter length of second rectangle:"))
b2=int(input("Enter breadth of second rectangle:"))
rect1_area=rectangle.area(l1,b1)
rect2_area=rectangle.area(l2,b2)
print("Area of first rectangle is:",rect1_area)
print("Area of second rectangle is:",rect2_area)
rect1_perimeter=rectangle.perimeter(l1,b1)
rect2_perimeter=rectangle.perimeter(l2,b2)
print("Perimeter of first rectangle is:",rect1_perimeter)
print("Perimeter of second rectangle is:",rect2_perimeter)
if(rect1_area>rect2_area):
    print("rectangle 1 has greater area")
else:
    print("rectangle 2 has greater area")
