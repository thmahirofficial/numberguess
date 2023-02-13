import random

def guess_the_number():
    print("\nWelcome to the 'Guess the Number' game!")
    print("I'm thinking of a number between 1 and 100.")
    print("Try to guess the number in as few attempts as possible.\n")
    
    number = random.randint(1, 100)
    attempts = 0
    
    while True:
        guess = int(input("Your guess: "))
        attempts += 1
        
        if guess < number:
            print("Too low.")
        elif guess > number:
            print("Too high.")
        else:
            print(f"Correct! You found the number in {attempts} attempts.")
            break

if __name__ == '__main__':
    guess_the_number()
