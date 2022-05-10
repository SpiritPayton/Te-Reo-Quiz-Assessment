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
            answer = "yes"
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
    print()
    print("The English word will mean the same food as one of the Te Reo words.")
    print("You will need to select which word you think (or hopefully know) it is.")
    print("There will be 10 rounds of questions. Above five right is a pass.")


# function to format text output
def formatter(symbol, text):
    sides = symbol * 3
    formatted_text = f"{sides} {text} {sides}"
    top_bottom = symbol * len(formatted_text)
    return f"{top_bottom}\n{formatted_text}\n{top_bottom}"


# answers
"bread" == "paraoa"
"cheese" == "tīhi"
"fish" == "ika"
"fruits" == "huarākau"


# Main routine goes here
print(formatter("-", "Kia ora! Are you ready to test your Te Reo Māori skills?"))
print()

print("You're about to learn how to say some kai names in Māori.")
print()
played_before = yes_no("Have you played this game before?: ").lower()
print()

if played_before == "no":
    instructions()


# begin game
