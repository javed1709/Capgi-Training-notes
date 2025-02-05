from abc import ABC,abstractmethod

class Employee(ABC):
    def __init__(self,name,salary):
        self.name=name
        self.salary=salary
    @abstractmethod
    def work():
        pass
    @abstractmethod
    def get_salary():
        pass

class Manager(Employee):
    def work(self):
        return f"{self.name} manages the team and overseeprojects"
    def get_salary(self):
        return self.salary
        
class Developer(Employee):
    def work(self):
        return f"{self.name} writes and debug the code"
    def get_salary(self):
        return self.salary
    
class Department:
        def __init__(self,name):
            self.name=name
            self.employess=[]

        def hire(self,emp):
            self.employess.append(emp)
            print(f"{emp.name} is hired in {self.name} department")
        
        def fire(self,emp):
            if emp in self.employess:
                self.employess.remove(emp)
                print(f"{emp.name} has fired from {self.name} department")
            else:
                print(f"{emp.name} is not in {self.name} department")
        def get_total_salary(self):
            return sum(employee.get_salary() for employee in self.employess)
        
        def show_employee_details(self):
            print(f"\n{self.name} Department Employee Details:")
            for emp in self.employess:
                print(f"- {emp.name}: {emp.work()} | Salary: {emp.get_salary()}")
            
manager1 = Manager("Alice", 80000)
dev1 = Developer("Bob", 60000)
dev2 = Developer("Charlie", 65000)

tech_dept = Department("Technology")

tech_dept.hire(manager1)
tech_dept.hire(dev1)
tech_dept.hire(dev2)

tech_dept.show_employee_details()

print(f"\nTotal Salary Expense: {tech_dept.get_total_salary()}")

tech_dept.fire(dev1)

tech_dept.show_employee_details()
