def square(num):
    return num**2

my_nums=[1,2,3,4,5]
map(square,my_nums)
list(map(square,my_nums))   # using Map funtion

def splicer(mystring):
    if len(mystring) %2 ==0:
        return 'even'
    else:
        return mystring[0]
    
mynames=['john','majid','chris','mike','sara']

list(map(splicer,mynames))     # USING MAP FUNCTION TOO.


def check_even(num):
    return num % 2 == 0

nums=[0,1,2,3,4,5,6,7,8,9,10]

list(filter(check_even,nums))   # FILTER FUNCTION

square = lambda num: num**2     # LAMBDA FUNCTION
sqaure(5)

list(map(lambda num: num**2 , my_nums))   # USING MAP AND LAMBDA
list(filter(lambda num: num % 2 ==0, nums)) # USING FILTER AND LAMBDA