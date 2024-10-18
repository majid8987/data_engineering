def myfunc(a,b):
    return sum((a,b)) *0.05

myfunc(40,60)

def myfunc(a=0,b=0,c=0,d=0,e=0,f=0):
    return sum((a,b,c,d,e,f)) *0.05

myfunc(40,60,20)


def myfunc(*args):                       #by using *kwargs we can take multiple choice
    return sum((args)) * 0.05

print(myfunc(40,60))
print(myfunc(40,60,20))
print(myfunc(10,20,30,40,50,60))