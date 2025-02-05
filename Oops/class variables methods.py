class Employee:
    company_name="ABC Corp"

    def __init__(self,name,age):
        self.name=name
        self.age=age

    @classmethod
    def change_company_name(cls,new_name):
        cls.company_name=new_name
    @staticmethod
    def smethod():
        print("I am static method for temporary task I am used")

    def display_info(self):
        print(f"Name: {self.name}, Age: {self.age},Company:{Employee.company_name}")


emp1=Employee("Alice",30)
emp2=Employee("Bob",25)

Employee.change_company_name("Capgemini")

emp1.display_info()
emp2.display_info()
emp1.smethod()
emp2.smethod()

