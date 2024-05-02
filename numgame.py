#numbergame
import random
num = random.randint(1,50)
guess = int(input(" can you your guess the number.Iam thinking ?It's less then 50 :"))
n = 0
while num!= guess:
    n += 1
    if n == 4:
        break
    if guess > num :
        print("your guess in higher")
    else:
        print("your guess is lower")

    guess = int(input("guess again:"))


