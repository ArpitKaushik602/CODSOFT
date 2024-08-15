import random

def get_computer_choice():
    """Randomly select rock, paper, or scissors for the computer."""
    return random.choice(['rock', 'paper', 'scissors'])

def determine_winner(user_choice, computer_choice):
    """Determine the winner based on user and computer choices."""
    if user_choice == computer_choice:
        return 'tie'
    elif (user_choice == 'rock' and computer_choice == 'scissors') or \
         (user_choice == 'scissors' and computer_choice == 'paper') or \
         (user_choice == 'paper' and computer_choice == 'rock'):
        return 'user'
    else:
        return 'computer'

def print_result(user_choice, computer_choice, winner):
    """Print the result of the game."""
    print(f"\nYour choice: {user_choice}")
    print(f"Computer's choice: {computer_choice}")
    if winner == 'tie':
        print("It's a tie!")
    elif winner == 'user':
        print("Congratulations! You win!")
    else:
        print("Sorry, you lose.")

def play_game():
    """Play the Rock-Paper-Scissors game with score tracking and replay option."""
    user_score = 0
    computer_score = 0

    print("Welcome to Rock-Paper-Scissors!")
    print("Type 'rock', 'paper', or 'scissors' to make your choice.")
    print("Type 'exit' to end the game.")

    while True:
        user_choice = input("\nEnter your choice: ").strip().lower()
        if user_choice == 'exit':
            print("\nThanks for playing!")
            break
        elif user_choice not in ['rock', 'paper', 'scissors']:
            print("Invalid choice. Please choose 'rock', 'paper', or 'scissors'.")
            continue

        computer_choice = get_computer_choice()
        winner = determine_winner(user_choice, computer_choice)
        print_result(user_choice, computer_choice, winner)

        if winner == 'user':
            user_score += 1
        elif winner == 'computer':
            computer_score += 1

        print(f"\nScore: You {user_score} - {computer_score} Computer")

        play_again = input("\nDo you want to play another round? (yes/no): ").strip().lower()
        if play_again != 'yes':
            print("\nThanks for playing!")
            break

if __name__ == "__main__":
    play_game()
