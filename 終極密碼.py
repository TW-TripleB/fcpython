
import random
maX=100
miN=1

ans=random.randint(1,100)
guess=0
while ans!=guess:
    guess=int(input("guess a number between 1~100:"))
    if guess>ans:
        maX=guess
        print("it's between",miN,"~",maX)
    elif guess<ans:
        miN=guess
        print("it's between",miN,"~",maX)
    else:
        guess==ans
        print("you won the game")
        break