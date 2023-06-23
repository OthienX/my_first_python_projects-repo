import random
secret_number = random.randint(1,20)
print("am  thinking of a numder different 1 and 20")
#ask the player to guess 6 times
for guesses_taken in range(1,7):
    print("take a guess ")
    guess = int(input())
    if  guess < secret_number:
      print("your guess is too low, make a right  guess please")
    elif guess > secret_number:
      print("youe guess is too high.")
    else:
          break
if guess == secret_number:
    print("well done, its a nice guess keep it up"+ str(guess))
else:
    print("its a wrong one it suppossed to be " +str(secret_number))