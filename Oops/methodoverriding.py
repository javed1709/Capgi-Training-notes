class Add: #single level inheritance
    def result(self,a,b):
        print("Adittion:",a+b)

class Multi(Add):
    def result(self,a,b):
        super().result(10,20) #Calling Parent
        print("Multiplication:",a*b)
    
m=Multi()
m.result(10,20)