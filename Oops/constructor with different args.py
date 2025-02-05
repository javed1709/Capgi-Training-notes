#constructor with *args 
class Example:
    def __init__(self, *args):
        if len(args)==1:
            print(f"Hello {args[0]}")
        elif len(args)==2:
            print(f"Hello {args[0]}, you are {args[1]} years")

#creating objects
obj1=Example("Alice")
obj1=Example("Bob",22)

# constructor with keywordargs
class Example:
    def __init__(self,**kwargs):
        if "name" in kwargs and "age" in kwargs:
            self.name=kwargs["name"]
            self.age=kwargs["age"]
            print(f"Hello {kwargs["name"]}, you are {kwargs["age"]} years old.")
        elif "name" in kwargs:
            self.name=kwargs["name"]
            print(f"hello {kwargs["name"]}")
    def display(self):
        print(f"Name = {self.name}\t")
    

obj1=Example(name="Alice")
obj1.display()
obj2=Example(name="Bob",age=30)