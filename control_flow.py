import random


secret = random.randint(1,5)
print("I am thinking of a number between 1 and 50...")
times = 0

while True: 
    guess = (input("Your guess:  "))
    if not guess.isdigit():
        print(f"Please enter a number!")
        continue
    guess = int(guess)
    times += 1
    if guess < secret:
        print("Too Low!")
    elif guess > secret:
        print("Too High")
    else:
        print(f"You guessed it in {times} times")
        break