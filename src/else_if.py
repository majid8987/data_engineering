P = int(input())
if P>=0:
    print(f"{P} is positive")
else :
    print(f"{P} is not positive")
    
    Y = int(input())
if Y > -10:
    print(f"{Y} is positive")
else : 
    print(f"{Y} is negative")
    
    z = int(input())
if z > -2:
    print(f"{z} is not 0")
else : 
    print(f"{z} is 0")
    
score = int(input())
if score > 90:
    print('Grade A')
elif 80 < score < 89 :
    print("Grade B")
elif 70 < score < 79:
    print("Grade C")
else:
    70 < score
    print("Grade D")

sum_number= sum([i for i in range(0,21)])

print(sum_number)

sum_number = [i for i in range(0,21)]
for i in sum_number:
    remainder = i%3
    if (remainder==0):
        print(f" {i} is divisible by 3")
    else:
        print(f"the remainder is {remainder} for the number{i}")
