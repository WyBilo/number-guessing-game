import random

def show_intro():
    print("\nWelcome to the Number Guessing Game")
    print("The system will pick a random number")
    print("You will guess a number 1 - 10")
    print("System will tell user if guess is high, low, or correct")
    print("Attempts will be recorded and shown upon correct answer")

def get_guess():
    while True:
        try:
            num = int(input("\nPlease pick a number: "))

            if 1 <= num <= 10:
                return num
            
            else:
                print("Please enter a number between 1 and 10. ")
            
        except ValueError:
            print("Invalid Input. Please enter a number 1 - 10.")
   

def play_game():
    rand_num = random.randint (1, 10) #Generates random number 1 - 10
    
    MAX_ATTEMPTS = 3
    attempts = 0

    while attempts < MAX_ATTEMPTS:
        guess = get_guess()
        attempts += 1

        if guess == rand_num:
            print("That is Correct!")
            break

        elif guess < rand_num:
            print("That's too low")

        else:
            print("That's too high")
        
        remaining = MAX_ATTEMPTS - attempts
        if remaining > 0:
            print(f"Wrong. Attempts remaining: {remaining}")
    
    if attempts == MAX_ATTEMPTS and guess != rand_num:
        print("You Lose.")


def main():
    show_intro()
    play_game()

main()