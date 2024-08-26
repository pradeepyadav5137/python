
f, g = eval(input("enter the center of the circle  "))
radius = eval(input("enter the radius of the circle  "))
x , y = eval(input("enter the point "))

# distace between the center and the point 
distance = ((y-g)**2 + (x-f)**2) ** 0.5

if distance < radius :
 print("The point is inside the circle")
elif distance > radius :
  print (" The Point is outside the circle")
else:
  print("The point is on the circle")


  