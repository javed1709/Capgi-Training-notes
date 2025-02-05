class PublicExample:
    def __init__(self,name):
        self.name=name
    def display(self):
        print(f"Name:{self.name}")

publicobj=PublicExample("Javed")
print(publicobj.name)
publicobj.display()
