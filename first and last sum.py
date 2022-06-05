n=int(input("Enter the number: "))
s=0
while n>0:           #2341>0   234>0           23>0    2>0   0>0
    rem=n%10         #rem=1    rem=234%10=4    rem=3   rem=2
    s=s+rem          #s=0+1=1   s=1+4          s=1+4+3  s=1+4+3+2
    n=n//10          #n=234     n=23            n=2     n=2//10=0
print("Sum of all digit is :",s)
    
      
