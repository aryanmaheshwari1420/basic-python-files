a=int(input("enter the first number: " ))
b=int(input("enter the second number: "))
if a<b:
    smaller=a
else:
    smaller=b
for i in range(smaller,1,-1):
    if a%i==0 and b%i==0:
        result=i
print(result)        
    
    
