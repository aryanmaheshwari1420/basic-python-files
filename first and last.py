n=int(input("Enter the number: "))   #6325  unit's place is 5 and last digit is 6
rem=n%10
while n>0:                       #6325>0      632>0      63>0   6>0  0>0
    t=n                          #t=6325      t=632      t=63   t=6
    n=n//10                      #n=632       n=63       n=6    n=0
print("First digit: ",rem)  
print("Last digit is :",t)
sum1=rem+t
print("sum is ",sum1)
