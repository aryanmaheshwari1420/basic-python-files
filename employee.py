class Employee:
    def __init__(self,name,age,salary,gender):
        self.name=name
        self.age=age
        self.salary=salary
        self.gender=gender


    def show_employee_details(self):
         print("name of employee is",self.name)
         print("age of person is ",self.age)
         print("salary of employe is",self.salary)
         print("gender o femployee is",self.gender)

e1=Employee('ram',32,5000,'male')         
