class Myclass:
    def sum(self,a=None,b=None,c=None): 
        '''method overloading Generally we write two functions with same name but
         here we are applying it by calling method with providing default value parameters  '''
        if a!=None and b!=None and c!=None:
            s=a+b+c
        elif a!=None and b!=None:
            s=a+b
        else:
            s="Provide atleast Two Numbers"
        return s

obj=Myclass()
print(obj.sum(10,20,30))
print(obj.sum(23,57))