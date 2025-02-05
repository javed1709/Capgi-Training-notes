from abc import ABC,abstractmethod
class Security(ABC):

    @abstractmethod
    def place_applied():
        pass

    @abstractmethod
    def material_used():
        pass

class Police(Security):

    def place_applied(self): # abstract inherited method (has self because to point the current obj memory)
        print("local Municipal")

    def material_used(self): # abstract inherited method (has self because to point the current obj memory)
        print("Announcing about projecct rag some activity")
    
class Navy(Security):
    def visit(self):
        print("Just to check the borderlines")
    
    def place_applied(self): # abstract inherited method (has self because to point the current obj memory)
        print("costal line")

    def material_used(self): # abstract inherited method (has self because to point the current obj memory)
        print("Announcing crossing border")

    
def main():
    police1=Police()
    police1.place_applied()
    police1.material_used()

    navy1=Navy()

    navy1.place_applied()
    navy1.material_used()
    navy1.visit()

main()