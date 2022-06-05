# program of square of no from 1 to 100 without using list comprehension

square=[]
for i in range(1,101):
    square.append(i**2)
print(square)





# program using lsit comprehension

squares=[i**2 for i in range(1,101)]

print(squares)


#cartesian product
A=[1,3,5,7]
B=[2,4,6,8]
cartesian_product=[(a,b) for a in A for b in B]
print(cartesian_product)




