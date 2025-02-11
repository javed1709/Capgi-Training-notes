from abc import ABC, abstractmethod
class Father(ABC):
    @abstractmethod
    def disp(self): # abstract method without body
        pass
    def show(self): # concrete method with body
        print("Concrete method")

from abc import ABC, abstractmethod
class Father(ABC):
    def display(self):
        print('I am display from Father abstract class')
    @abstractmethod
    def myAbstractMethod(self):
        pass
class Child(Father):
    def myAbstractMethod(self):
        print('Hello from Child class implementing abstract method')
    def show(self):
        print("Show method from child class")

c=Child()
c.show()
c.myAbstractMethod()