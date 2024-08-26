print("Equaion: a1x+b1y+c1z+d1=e1, four unknowns x,y,z,w")

a1,b1,c1,d1,e1=eval(input("For equation one:"))
a2,b2,c2,d2,e2=eval(input("For equation two:"))
a3,b3,c3,d3,e3=eval(input("For equation three:"))
a4,b4,c4,d4,e4=eval(input("For equation fout:"))

det=a1*(b2*(c3*d4-d3*c4)-c2*(b3*d4-d3*b4)+d2*(b3*c4-b4*c3))-b1*(a2*(c3*d4-d3*c4)-c2*(a3*d4-d3*a4)+d2*(a3*c4-a4*c3))+c1*(a2*(b3*d4-d3*b4)-b2*(a3*d4-d3*a4)+d2*(a3*b4-a4*b3))-d1*(a2*(b3*c4-c3*b4)-b2*(a3*c4-c3*a4)+c2*(a3*b4-a4*b3))

detX=e1*(b2*(c3*d4-d3*c4)-c2*(b3*d4-d3*b4)+d2*(b3*c4-b4*c3))-b1*(e2*(c3*d4-d3*c4)-c2*(e3*d4-d3*e4)+d2*(e3*c4-e4*c3))+c1*(e2*(b3*d4-d3*b4)-b2*(e3*d4-d3*e4)+d2*(e3*b4-e4*b3))-d1*(e2*(b3*c4-c3*b4)-b2*(e3*c4-c3*e4)+c2*(e3*b4-e4*b3))

detY=a1*(e2*(c3*d4-d3*c4)-c2*(e3*d4-d3*e4)+d2*(e3*c4-e4*c3))-e1*(a2*(c3*d4-d3*c4)-c2*(a3*d4-d3*a4)+d2*(a3*c4-a4*c3))+c1*(a2*(e3*d4-d3*e4)-e2*(a3*d4-d3*a4)+d2*(a3*e4-a4*e3))-d1*(a2*(e3*c4-c3*e4)-e2*(a3*c4-c3*a4)+c2*(a3*e4-a4*e3))

detZ=a1*(b2*(e3*d4-d3*e4)-e2*(b3*d4-d3*b4)+d2*(b3*e4-b4*e3))-b1*(a2*(e3*d4-d3*e4)-e2*(a3*d4-d3*a4)+d2*(a3*e4-a4*e3))+e1*(a2*(b3*d4-d3*b4)-b2*(a3*d4-d3*a4)+d2*(a3*b4-a4*b3))-d1*(a2*(b3*e4-e3*b4)-b2*(a3*e4-e3*a4)+e2*(a3*b4-a4*b3))

detW=a1*(b2*(c3*e4-e3*c4)-c2*(b3*e4-e3*b4)+e2*(b3*c4-b4*c3))-b1*(a2*(c3*e4-e3*c4)-c2*(a3*e4-e3*a4)+e2*(a3*c4-a4*c3))+c1*(a2*(b3*e4-e3*b4)-b2*(a3*e4-e3*a4)+e2*(a3*b4-a4*b3))-e1*(a2*(b3*c4-c3*b4)-b2*(a3*c4-c3*a4)+c2*(a3*b4-a4*b3))

print("Value of Det: ",det)
print("Value of DetX: ",detX)
print("Value of DetY: ",detY)
print("Value of DetZ: ",detZ)
print("Value of DetW: ",detW)

if det!=0:
    x=detX/det
    y=detY/det
    z=detZ/det
    w=detW/det
    print("The value of all four unknowns : ",x,y,z,w)