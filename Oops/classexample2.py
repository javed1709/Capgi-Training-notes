class Employee:
    def __init__(self,name,gender,salary):
        self.employeeName=name
        self.gender=gender
        self.salary=salary
    
    def get_employee_details(self):
        print(f"Name :{self.employeeName} Gender: {self.gender} Salary: {self.salary}")
    
# employee1=Employee("Yash","male",1234)
# employee2=Employee("Tina","female",3412)
# employee3=Employee("Javed","male",4328)

# employee1.get_employee_details()
# employee2.get_employee_details()
# employee3.get_employee_details()

n=int(input("Enter no of employees:"))

employees=[]

for i in range(n):
    print(f"\nEnter details for Employess {i+1}:")
    name=input("Enter employee name:")
    gender=input("Enter employee gender:")
    salary=float(input("Enter the employeee salary"))

    employee=Employee(name,gender,salary)

    employees.append(employee)

for i in employees:
    i.get_employee_details()

chk=bool(input("Enter the choice:"))
# m=lambda x:(x.gender=="Male" and x.get_employee_details())
# f=lambda x:(x.gender=="Female" and x.get_employee_details())
tell=lambda x,chk:((x.gender=="Male" and x.get_employee_details()) if chk==True else (x.gender=="Female" and x.get_employee_details()))
for i in employees:
    # if chk: m(i)
    # else: f(i)
    tell(i,chk)










