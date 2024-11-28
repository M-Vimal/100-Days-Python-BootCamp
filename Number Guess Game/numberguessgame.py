import random

print("Welcome To Number Guess Gmae!")
print("I'm thinking of a number between 1 to 100")
difficulty = input("Choose Difficulty.Type 'EASY' or 'HARD' :").lower()

#computer guess answer
answer = random.randint(1,101)

if difficulty == 'easy':
    print("You have 10 attempts to guess")
    for i in range(10,0,-1):
        guess = int(input("make your guess:"))
        if guess == answer:
            print(f"You Won")
            break
        elif guess > answer:
            print("Too high")
            print("Guess again")
            print(f"you have {i-1} chances left")
        elif guess < answer:
            print("Too low")
            print("Guess again")
            print(f"you have {i-1} chances left")
    print(f"you lost.my guess is {answer}")
        
if difficulty == 'hard':
    print("You have 5 attempts to guess")
    for i in range(5,0,-1):
        guess = int(input("make your guess:"))
        if guess == answer:
            print(f"You Won")
            break
        elif guess > answer:
            print("Too high")
            print("Guess again")
            print(f"you have {i-1} chances left")
        elif guess < answer:
            print("Too low")
            print("Guess again")
            print(f"you have {i-1} chances left")
    print(f"you lost.my guess is {answer}")



