# class Car:
#     def __init__(self):
#         print("Car class constructor")
#     def showF(self):
#         print("Father class method")
#     def type():
#         print("Type is:Petrol")

# class Innova(Car):
#     def __init__(self):
#         super().__init__()
#         print("Innova class constructor")
#     def showS(self):
#         print("Innova class method")
#     def model(self):
#         print("xyz")

# class Cresta(Innova):
#     def __init__(self):
#         super().__init__()
#         print("Cresta class constructor")
#     def showG(self):
#         print("Cresta class method")

# g=Cresta()
# g.showG()
# g.showF()
# g.showS()

# class Book:
#     library={}
#     def __init__(self):
#         self.library={}

#     def add_book(self,isb,book_details):
#         if self.library.get(isb,False)==False:
#             self.library[isb]=book_details
#         else:
#             self.library[isb][2] +=1
    
#     def find_book(self,isbn):
#         return self.library[isbn]
    
#     def remove_book(self,isbn):
#         if self.library[isbn][2]>0:
#             self.library[isbn][2] -=1
#         else:
#             del self.library[isbn]
#     def display_library(self):
#         # for i in self.library:
#         #     lst=list(self.library[i])
#         #     print(f"isbn:{i}, Title:{lst[0]} , Author: {lst[1]}, no of copies lst[2]")
#         print(self.library)


# b1,b2,b3=Book(),Book(),Book()
# b1.add_book("1234567891012",["Trignometry","G.tiwani",12])
# b2.add_book("2234567891012",["Trignometry","G.riwani",14])
# b3.add_book("3234567891012",["Trignometry","G.siwani",18])
# b1.display_library()
# b1.remove_book("1234567891012")
# b1.display_library()
# b2.display_library()
# b2.remove_book("2234567891012")
# b3.display_library()
# b3.remove_book("3234567891012")




class Employee:
    def __init__(self, name, age, salary, department, role):
        self.name = name
        self.age = age
        self.salary = salary
        self.department = department
        self.role = role

    def display_employee_info(self):
        print(f"Name: {self.name}, Age: {self.age}, Salary: {self.salary}, Department: {self.department}, Role: {self.role}")

class Manager(Employee):
    def __init__(self, name, age, salary, department):
        super().__init__(name, age, salary, department, "Manager")

class Engineer(Employee):
    def __init__(self, name, age, salary, department, skills):
        super().__init__(name, age, salary, department, "Engineer")
        self.skills = skills

    def display_employee_info(self):
        super().display_employee_info()
        print(f"Skills: {', '.join(self.skills)}")

class Company:
    def __init__(self):
        self.departments = {}

    def add_employee(self, employee):
        if employee.department not in self.departments:
            self.departments[employee.department] = []
        self.departments[employee.department].append(employee)

    def find_manager(self, department):
        for emp in self.departments.get(department, []):
            if emp.role == "Manager":
                return emp
        return None

    def count_employees_in_department(self, department):
        return len(self.departments.get(department, []))

    def count_engineers_with_skill(self, skill):
        count = 0
        for dept in self.departments.values():
            for emp in dept:
                if emp.role == "Engineer" and skill in emp.skills:
                    count += 1
        return count

    def display_total_employees_in_department(self):
        for dept, employees in self.departments.items():
            print(f"Total employees in {dept}: {len(employees)}")

    def display_total_employees(self):
        total = sum(len(employees) for employees in self.departments.values())
        print(f"Total employees in the company: {total}")

# Example usage
company = Company()

# Adding employees
company.add_employee(Manager("Alice", 45, 90000, "HR"))
company.add_employee(Employee("Bob", 30, 50000, "HR", "Employee"))
company.add_employee(Employee("Charlie", 25, 40000, "HR", "Employee"))

company.add_employee(Manager("Dave", 50, 100000, "Engineering"))
company.add_employee(Engineer("Eve", 35, 80000, "Engineering", ["Python", "C++"]))
company.add_employee(Engineer("Frank", 28, 70000, "Engineering", ["Java", "Python"]))
company.add_employee(Engineer("Grace", 32, 75000, "Engineering", ["C#", "Python"]))

# Finding manager for a department
manager = company.find_manager("HR")
if manager:
    print(f"Manager of HR: {manager.name}")

# Counting employees in a department
print(f"Total employees in Engineering: {company.count_employees_in_department('Engineering')}")

# Counting engineers with a specific skill
print(f"Engineers with Python skill: {company.count_engineers_with_skill('Python')}")

# Total employees in each department
company.display_total_employees_in_department()

# Total employees in the company
company.display_total_employees()