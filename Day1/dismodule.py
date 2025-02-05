import dis

def add(a,b):
    return a+b

print(f"Result of add function:{add(6,4)}")

dis.dis(add)