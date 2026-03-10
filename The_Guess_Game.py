import random

print("Welcome To The Number Guessing Game!")
print("Guess a number between 1 and 100")

n = random.randint(1, 100)
a = -1
guess = 1
while(a != n):
    a = int(input("Guess the number: "))
    if(a > n):
        print("Lower Number Please")
        guess += 1
    elif(a < n):
        print("Higher Number Please")
        guess +=1

print(f"Correct! The number was {n}.")
print(f"You have guessed the number {n} correctly in {guess} attempts")

# Score System
if (guess <= 4):
    print("🏆  Score : Genius!")
elif(guess <=7):
    print("👍  Score : Good!")
else:
    print("😅  Score : Try Again!")