def myfunc(**kwargs):
    if 'fruit' in kwargs:
        print(f"my fav fruits is {kwargs['fruit']}")
    else :
        print('i dont like fruits')

myfunc(fruit='pineapple')
myfunc()
