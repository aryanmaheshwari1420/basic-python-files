p1=int(input())
p2=int(input())
s=p1+p2
if p1>499 and p2>499:
    d=0
elif p1<500 and p2<499:
    d=80
elif p1<500 and p1>499:
    d=40
elif p2<500 and p1>499:
    d=40
s=s+d
print("total cost of the product is ",s)
    
