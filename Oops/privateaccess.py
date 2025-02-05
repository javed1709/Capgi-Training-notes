class PrivateExample: #Private attributes and methods are accessable within the class only
    def __init__(self,name):
        self.__name=name

    def __display(self):
        print(f"Name is : {self.__name}")
    def accessing_private(self):
        print(self.__name)
        self.__display()

privateobj=PrivateExample("rayon")
# print(privateobj.__name) ❌
# privateobj.__display()  ❌
privateobj.accessing_private() #✅
print(privateobj._PrivateExample__name) # accessing private attributes explicitly using this kind of syntax (but not recommended)
privateobj._PrivateExample__display()
