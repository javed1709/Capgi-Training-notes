class Father:
    def __init__(self):
        print("Father class constructor")
    def showF(self):
        print("Father class method")

class Son(Father):
    def __init__(self):
        super().__init__()
        print("Son class constructor")
    def showS(self):
        print("Son class method")

class Grandson(Son):
    def __init__(self):
        super().__init__()
        print("Grandson class constructor")
    def showG(self):
        print("Grandson class method")

g=Grandson()
g.showG()
g.showF()
g.showS()