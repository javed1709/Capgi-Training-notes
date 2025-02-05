#is / not it
x,y=2,5
print(x is y)
print(x is not y)

def iks_prime(n):
    i=2
    while (i*i+1)<=n:
        if n%i==0:
            return False
        i +=1
    return True

print(iks_prime(15))