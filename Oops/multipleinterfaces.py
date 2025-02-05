from abc import ABC,abstractmethod

class interface1(ABC):
    @abstractmethod
    def show1():
        pass

class interface2(ABC):
    @abstractmethod
    def show2():
        pass

class DerivedClass(interface1,interface2):
    def show1(self):
        print("show method of an interfacel invoked")

    def show2(self):
        print("show method of an interfacel invoked")
    
derivedClass=DerivedClass()
derivedClass.show1()
derivedClass.show2()