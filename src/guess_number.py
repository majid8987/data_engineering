from random import randint
randint(1,20)
while True:
    guess= int(input("guess a number between 1 and 20 :"))
if guess <1 or guess > 10:
    print("please choose a number withn in a range")
elif randint(1,20) < guess:
    print("try again")
elif randint(1,20) > guess:
    print("too close ! try again")
else:
    print("congratulation you guess the number")