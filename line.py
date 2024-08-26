x1 , y1 , x2, y2 = eval(input("enter both point of first line  "))

x3 , y3 , x4, y4 = eval(input("enter both point of second line  "))

#equation of first line 

m1 = (y2-y1)/(x2-x1)
m2 = (y4-y3)/(x4-x3)


D = m2-m1 

dx =(m2*y3 - y3 )-(m1*x1 -  y1 )

dy = m1 *((m2*y3 - y3 )) - m2 * (m1*x1 - y1 )

x = dx/D
y = dy/D

print(" x " , x , " y " , y )


# enter both point of first line  -1,-1,-2,2
# enter both point of second line  -2,-2,-6,2
#  x  0.0  y  -4.0