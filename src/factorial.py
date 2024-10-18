def factorial(number):
    if number == 1:
        return 1 
    result = 1
    for num in range(1,8):
          result *= num
    return result
          
   
factorial(7)
