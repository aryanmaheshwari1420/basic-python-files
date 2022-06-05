n=int(input("no  "))
c=0
for i in range(1,n):
    if n%i==0:
        c=c+1
if c==1:
    print("prime")
else:
    print("not prime")

        
        
n=int(input("no  "))
c=0
for i in range(2,n+1):
    if n%i==0:
        c=c+1
if c==1:
    print("prime")
else:
    print("not prime")
