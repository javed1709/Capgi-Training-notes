
#ploymorphism:strong typing
class Cat:
    def talk(self):
        print("Cat says i am hungry")
    
def myfunction(obj): # duck method takes any class instance
    if hasattr(obj,"walk"):
        obj.walk()
    if hasattr(obj,"talk"):
        obj.talk()

class Duck:
    def walk(self):
        print("Duck says i am hungry")
    
class Horse:
    def walk(self):
        print("Horse says i am hungry")
    # pass

d=Duck()
myfunction(d)

h=Horse()
myfunction(h)

c=Cat()
myfunction(c)