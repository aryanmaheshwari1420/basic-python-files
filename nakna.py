
l1=[2,5,1,6,8,4]
even=[]
odd=[]
sum1=0
sum2=0
for i in l1:
    if i%2==0:
        even.append(i)
    else:
        odd.append(i)
for j in even:
    sum1=sum1+j
for k in odd:
    sum2=sum2+k
print(even,odd)
print(sum1,sum2)
    
    

