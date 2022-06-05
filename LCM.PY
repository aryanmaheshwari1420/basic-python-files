a=int(input("enter the first no: "))
b=int(input("enter the second no:"))
if a>b:
    greater=a
else:
    greater=b
for i in range(greater,a*b+1):
    if greater%a==0 and greater%b==0:
        result= greater
        break
    else:
        greater=greater+1
print(greater)        
