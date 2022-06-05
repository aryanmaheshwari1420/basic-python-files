#HCF=HIGHEST COMMON FACTOR
#GCD=GREATEST COMMON DIVISOR


#25=5*5
#50=2*5*5
#HCF=5*5=25

a=int(input("enter the first number: "))
b=int(input("enter the second number:"))
if a<b:
    smaller=a
else:
    smaller=b
for i in range(1,smaller+1):          #possible divisor #gcd is always lesser than the smaller no among them
            if a%i==0 and b%i==0:
                result=i              #result contain common divisor and as result contain 2 value so it update the last one
print(result)                
