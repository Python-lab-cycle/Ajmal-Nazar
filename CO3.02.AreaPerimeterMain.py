from Graphics.RectangleFunction import*
from Graphics.CircleFunction import *
from Graphics.DGraphics.SphereFunction import *
from Graphics.DGraphics.CuboidFunction import *
while[True]:
    print("\n**Menu**")
    print("\n1.Rectangle")
    print("\n2.Circle")
    print("\n3.Sphere")
    print("\n4.Cuboid")
    print("\n5.Quit")
    print("********")
    choice=int(input("Enter Choice:"))
    if(choice==1):
        l1=int(input("Enter Length:"))
        b1=int(input("Enter Breadth:"))
        area=rectanglearea(l1,b1)
        print("\nArea is:"+str(area))
        perimeter=rectangleperimeter(l1,b1)
        print("\nPerimeter is:" + str(perimeter))
    elif(choice==2):
        r1=int(input("Enter Radius:"))
        area=circlearea(r1)
        print("\nArea is:"+ str(area))
        perimeter=circleperimeter(r1)
        print("\nPerimeter is:"+ str(perimeter))
    elif(choice==3):
        r1=int(input("Enter Radius:"))
        area=spherearea(r1)
        print("\nArea is:" + str(area))
        perimeter=sphereperimeter(r1)
        print("\nPerimeter is:" + str(perimeter))
    elif(choice==4):
        l1=int(input("Enter Length:"))
        w1=int(input("Enter Width:"))
        h1=int(input("Enter Heigth:"))
        area=cuboidarea(l1,w1,h1)
        print("\nArea is:" + str(area))
        perimeter=cuboidperimeter(l1,w1,h1)
        print("\nPerimeter is:" + str(perimeter))
    elif(choice==5):
        quit(0)
    else:
        print("Enter a valid choice")
