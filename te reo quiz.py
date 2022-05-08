"""Te Reo foods quiz
"""
import random


# yes/no checking function
def yes_no(question_text):
    while True:

        # ask user if they have played the game before
        answer = input(question_text).lower()

        # if they say yes, continue program
        if answer == "yes" or answer == "y":
            answer = "Yes"
            return answer

        # if they say no, display instructions
        elif answer == "no" or answer == "n":
            answer = "no"
            return answer

        # otherwise, show error
        else:
            print("Don't be weird. Just enter 'yes' or 'no'.")


# Function to display instructions
def instructions():
    print(formatter("*", "How to play"))
    print()
    print("I'm going to give you four names of food in Te Reo,")
    print("then the name of a food in English.")
    print("The English word will be the same food as one of the Te Reo words.")
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


# Main routine goes here
print(formatter("-", "Kia ora! Are you ready to test your Te Reo Māori skills?"))
print()

print(formatter("-", "You're about to learn how to say some kai names in Māori."))
print()
played_before = yes_no("Have you played this game before?: ").lower()
print()

if played_before == "no":
    instructions()
