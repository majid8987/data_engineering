#Combining *args and **kwargs :

def myfunc(*args,**kwargs):
    if 'fruit' and 'juice' in kwargs:
        print(f"I like  {'  and  '.join(args)} and my fav fruit is {kwargs['fruit']}")
        print(f"may i have some {kwargs['juice']} juice?")
    else :
        pass

myfunc('eggs',fruit = 'cherries', juice = 'orange')