maxf = lambda x, y : x if x > y else y
maxf(65,60)

words = ['madam','hello','racecar','world','level']
list(map(lambda word : word == word[::-1],words))      # these shows True or False
 
words = ['madam','hello','racecar','world','level']
list(filter(lambda word : word == word[::-1],words))

