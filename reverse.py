n=int(input("Enter the number: "))
s=0
while n>0:        #1234>0           123>0
    rem=n%10      #rem=1234%10=4    rem=3
    s=s*10+rem    #s=0*10+4          s=4*10+3
    n=n//10       #n=1234//10=123    n=123//n
print(s)
    
