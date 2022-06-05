s=0
x=int(input())
n=int(input())
for i in range(1,n+1):
    s=s+(-1)**(i-1)*(x**i)/i
print(s)
