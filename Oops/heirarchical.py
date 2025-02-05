class Father():
    def __init__(self):
        print("Father class constructor")
    def showF(self):
        print("Father class method")

class Son(Father):
    def __init__(self):
        print("Son class constructor")
    def showS(self):
        print("Son class method" )

class Daughter(Father):
    def __init__(self):
        print("Daughter class constructor")
    def showG(self):
        print("Daughter class method")

d=Daughter()
d.showG()
d.showF()
s=Son()
s.showS()
s.showF()