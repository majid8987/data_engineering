#3. a. Write a code to print all the Prime Number until the range specified:
 #     example- 10: 2,3,5,7
  # b. Write a program that determines whether the number is prime or not
   #   example- 45 -- 45 is not a prime number
    #   97 - 97 is  prime number 
    
    # prime number range

num = 20
l = []
l.append(2)
for i in range(3, num+1,2):
    count=0
    for j in range(1,i+1):
        if i % j == 0:
            count = count+1
    if count == 2:
        l.append(i)

print(f"Prime Number until {num} are {l}")

#code 2

count = 0 
num = 18
if num <= 1:
    print(f"{num} is not a prime number")
if num == 2 or num == 3:
    print(f"{num} is a prime number")
for i in range(4, num+1,):
    if num % i == 0:
        count = count+1
    if count == 2:
        print(f"{num} is a Prime")
    else:
        print(f"{num} is not a prime")