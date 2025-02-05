class ProtectedExample:
    def __init__(self,name):
        self._name=name
    def _display(self):
        print(f"Name: {self._name}")

class SubClass(ProtectedExample):
    def show(self):
        print(f"Acessing protected {self._name}")
        self._display()
    
# protectedobj=ProtectedExample("Jiangly")
# print(protectedobj._name)
# protectedobj._display()
subclassobj=SubClass("tourist")
subclassobj.show()