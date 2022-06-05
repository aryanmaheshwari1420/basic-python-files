p1=int(input())
p2=int(input())
s=p1+p2
if p1>499:
    if p2>499:
        d=0
    else:
        d=40
else:
    if p2<500:
        d=80
    else:
        d=40
s=s+d
print("total cost of the product is ",s)
        
