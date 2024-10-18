name=input()
print(f" hi {name}")

list(range(0,11,1))

list(range(0,13,5))

#enumerate

index = 0
for letter in 'abcdefg':
    print('at index {} the letter is {}'.format(index,letter))
    index+=1
    
    
for index,letter in enumerate('abcdefg'):
     print('at index {} the letter is {}'.format(index,letter))
     
     list(enumerate('abcdefg'))