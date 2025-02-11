class Employee:
    def __init__(self):
        print("I am a default init method")
    
    def __init__(self,name):
        self.name=name #self.name will become the class variable
        print(f"I am a init method with name parameter {name}")

    def demomethod(self):
        print("I am a demo method from Employee")
        print(self.name)


employee1=Employee()
employee2=Employee("Javed")
employee2.demomethod()
    
#in python there should be only constructor if we multiple then the last constructor we write will be overridden to all previous one