import random

def get_feedback():
    """Prompt the user for feedback and return it."""
    feedback = input("We'd love to hear your feedback! Please provide any comments or suggestions: ")
    print("Thank you for your feedback!")
    return feedback

def main():
    """Main function to run the Rock, Paper, Scissors game."""
    print("Welcome to Rock, Paper, Scissors Game")

    while True:
        Comp = random.randint(1, 3)
        user = int(input("Choose 1 for Rock, 2 for Paper, and 3 for Scissors: "))

        if user == Comp:
            print(f"Draw! Computer also chose {Comp}")

        elif (user == 1 and Comp == 2) or (user == 3 and Comp == 2) or (user == 2 and Comp == 1):
            print(f"You Lose! Computer chose {Comp}")

        elif (user == 1 and Comp == 3) or (user == 2 and Comp == 3) or (user == 3 and Comp == 1):
            print(f"You Won! Computer chose {Comp}")

        else:
            print("Invalid choice! Please choose 1 for Rock, 2 for Paper, or 3 for Scissors.")

        Again = input("If you want to play again, press *; to exit, press #: ")
        if Again == "#":
            # Call the feedback function before exiting
            get_feedback()
            break

    print("Thank you for playing!")

if __name__ == "__main__":
    main()
