class Vehicle:
    def __init__(self,mileage,cost):
        self.mileage=mileage
        self.cost=cost

    def show_vehicle_details(self):
        print("mileage of vehicle is",self.mileage)
        print("cost of vehicle is",self.cost)

v1=Vehicle(500,500)

class car(Vehicle):
    def show_car_details(self):
        print("i m a car")
c1=car(250,500)        


        



    
