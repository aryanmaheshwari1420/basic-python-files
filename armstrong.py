n=int(input("Enter the number: "))
x=n
c=0
while x>0:
    c=c+1
    x=x//10
s=0
t=n
while n>0:
    rem=n%10    #individual digit
    s=s+rem**c    #s=3**3+5**3+1**3
    n=n//10      #number reduce
if s==t:
    print("Armstrong")
else:
    print("Not armstrong")
