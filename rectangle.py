height = eval(input("enter height "))
width = eval(input("enter width "))

x,y = eval(input( "enter point "))

if abs(y) < height/2 and abs(x) < width/2:
       print("the point is in the rectangle")
elif  abs(y) == height / 2 and abs(x) == width / 2:
       print(" the point is on the rectangle")
else:
    print ("point is out side of the rectangle")
