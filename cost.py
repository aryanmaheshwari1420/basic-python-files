Qt=int(input("enter the price"))
total_cost= Qt*100
if(total_cost>1000):
    total_cost= total_cost - (total_cost*10/100)
    print("done")
print(total_cost)
