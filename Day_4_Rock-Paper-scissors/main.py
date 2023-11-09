import random

# ASCII Art for the game
rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

# Function to print ASCII Art based on the choice
def print_choice(choice):
    if choice == 1:
        print(rock)
    elif choice == 2:
        print(paper)
    elif choice == 3:
        print(scissors)

# Function to simulate the game
def play_game():
    # Print the welcome message
    print(welcome)
    
    # Ask the user for their choice
    user_choice = input("Enter 1 for Rock, 2 for Paper, or 3 for Scissors: ")
    
    # Check if the input is valid
    if user_choice not in ['1', '2', '3']:
        return "Invalid selection! Please enter 1, 2, or 3."
    
    # Convert the user_choice from string to int
    user_choice = int(user_choice)
    
    # Generate a random number for the computer's choice
    computer_choice = random.randint(1, 3)

    # Print user's choice in ASCII Art
    print("Your choice:")
    print_choice(user_choice)

    # Print computer's choice in ASCII Art
    print("Computer's choice:")
    print_choice(computer_choice)

    # Determine the winner
    if user_choice == computer_choice:
        return "It's a tie!"
    elif (user_choice == 1 and computer_choice == 3) or \
         (user_choice == 2 and computer_choice == 1) or \
         (user_choice == 3 and computer_choice == 2):
        return "You win!"
    else:
        return "You lose!"
    

# Welcome message
welcome = '''
Welcome to Our Rock Paper Scissors Game!!!!

The Winner will be a best out of Three.

The Rules are as followed:
Rock wins against scissors.
Scissors win against paper.
Paper wins against rock.

When the Game starts you will be Prompted:

"Rock, Paper, Scissors, Shoot!" or “1, 2, 3, Shoot!!!

Enter 1 for Rock
Enter 2 for Paper
Enter 3 for Scissors
'''

 # Start the game and get the result
result = play_game()
print(result)
