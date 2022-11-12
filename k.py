def funct(n):
    return lambda s:s/n
n=int(input("enter a number"))
s=int(input("enyr a value for s"))
x=funct(n)
print(x(s))
