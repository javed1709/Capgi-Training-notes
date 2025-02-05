# Actually for abstract class no abject cannot be created and constructor can't be called
# but we can do using super keyword through derived class
from abc import ABC,abstractmethod

class AbstractBase(ABC):
    def __init__(self,value):
        self.value=value
        print("Abstract class is called")
    
    @abstractmethod
    def show(self):
        pass

class ConcreteClass(AbstractBase):
    def __init__(self,value,extra):
        super().__init__(value)
        self.extra=extra
        print("ConcreteClass constructor called")

    def show(self):
        print(f"Value: {self.value}, Extra: {self.extra}")

obj=ConcreteClass(10,"extra data")
obj.show()

