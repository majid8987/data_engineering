a= {2,4,6,3,7,8,4.5,-1,-3,0}
b={1,2,4,3,6,8,9,5,-4,-6,3.5}

print(type(a))
print(type(b))
print(a)
print(b)

print(a|b) #union |
print(a&b) # intersection &
print(a-b) # difference
print(a^b) # symmetric diff ^

d= a|b    #removing duplicates
print(d)

e = a.add(10)  #adding an element
a

r= a.remove(4.5) #removing an element
r
