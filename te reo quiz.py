"""Te Reo foods quiz
"""
import random


# yes/no checking function
def yes_no(question_text):
    while True:

        # Ask user if they have played the game before
        answer = input(question_text).lower()

        # If they say yes, output "Program Continues"
        if answer == "yes" or answer == "y":
            answer = "Yes"
            return answer

        # If they say no, output "Display Instructions"
        elif answer == "no" or answer == "n":
            answer = "no"
            return answer

        # Otherwise, show error
        else:
            print("Please enter 'yes' or 'no'.")


# Function to display instructions
def instructions():
    print(formatter("*", "How to play"))
    print()
    print("Choose a starting amount to play with - must be between $1 and $10")
    print()
    print("Then press <enter> to play. You will get a random token"
          " which might "
          "be a horse, a zebra, a donkey, or a unicorn")
    print()
    print("It costs $1 to play each round but, depending on your prize, you "
          "could win some money back. These are the payout amounts:\n"
          "\tUnicorn : $5 (balance increases by $4\n"
          "\tHorse : $0.50 (balance decreases by $0.50\n"
          "\tZebra : $0.50 (balance decreases by $0.50\n"
          "\tDonkey : $0 (balance decreases by $1\n")
    print("\nSee if you can avoid donkeys, get the unicorns, and finish with "
          "more money than you started with.")


# function to format text output
def formatter(symbol, text):
    sides = symbol * 3
    formatted_text = f"{sides} {text} {sides}"
    top_bottom = symbol * len(formatted_text)
    return f"{top_bottom}\n{formatted_text}\n{top_bottom}"
