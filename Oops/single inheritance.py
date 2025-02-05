class Employee:

    def __init__(self,name,designation):
        self.name=name
        self.designation=designation
    
    def get_employee_details(self):
        print(f"Employee Name : {self.name} \n Designation : {self.designation}")
    
class ContractEmployee(Employee):
    def __init__(self,name,designation,contract_period):
        super().__init__(name,designation)
        self.contract_period=contract_period

    def get_contract_Employee_details(self):
        print(f"Contract period is {self.contract_period}")

c_employee1=ContractEmployee("Lalitha","Senior Consultant", "3years")
c_employee1.get_employee_details()
c_employee1.get_contract_Employee_details()