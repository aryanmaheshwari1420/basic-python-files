m1=int(input("enter the marks : "))
m2=int(input("enter the marks : "))
m3=int(input("enter the marks : "))
if m1<=100 and m2<=100 and m3<=100:

    s=m1+m2+m3
    average=s/3

    if average>90:
        print("excellent")
    elif average<=89:
        print("good")
    elif average<=79:
        print("average")

    
