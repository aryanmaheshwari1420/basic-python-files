a=int(input("enter the first side:"))
b=int(input("enter the second side:"))
c=int(input("enter the third side:"))
if a+b>c and b+c>a and c+a>b:
    height=pow((b**2+c**2),1/2)
    AREA=1/2*b*height
    print("area of scalene triangle is ",AREA)
else:
    print("invalid sides")
