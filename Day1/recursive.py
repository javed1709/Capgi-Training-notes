
def say(n):
    if n==0:
        print("Exceeded the limit of recursion")
        return
    print("goining deep by creating a recursive stack")
    say(n-1)

say(4)