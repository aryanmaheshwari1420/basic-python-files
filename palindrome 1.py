n=int(input("Enter the number: "))

for n in range(n,1000):
    t=n
    s=0
    while n>0:
        rem=n%10
        s=s*10+rem
        n=n//10
    if t==s:
        print(t)
