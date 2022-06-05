a=int(input("enter the start range"))
b=int(input("enter the last range"))
for i in range(a,b+1):
    if i%2!=0:
        print("",i,end="")
