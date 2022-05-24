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
    print("Let's begin!")
    print()
    print()


# function to format text output
def formatter(symbol, text):
    sides = symbol * 3
    formatted_text = f"{sides} {text} {sides}"
    top_bottom = symbol * len(formatted_text)
    return f"{top_bottom}\n{formatted_text}\n{top_bottom}"


# while loop to play the quiz again or exit
play_again = ""


# Main routine goes here
score = 0
print(formatter("-", "Kia ora! Are you ready to test your Te Reo Māori skills?"))
print()

print("You're about to learn how to say some kai names in Māori.")
print()
played_before = yes_no("Have you played this game before?: ").lower()
print()

if played_before == "no":
    instructions()


# begin game - question 1
while play_again != "X":
    answer1 = input("What is the Maori word for bread? \na. paraoa \nb. ika \nc. hupa\n\n").lower()
    if answer1 == "a" or answer1 == "paraoa":
        score += 1
        print("Paki paki! Ka pai!")
        print("\n")
    else:
        print("Racist Pākehā, you're wrong. Stop colonising Aotearoa.")
        print("Score: ", score)
        print("\n")

    # question 2
    answer2 = input("What is the Maori word for meat? \na. kawhe \nb. huamata \nc. mīti\n\n").lower()
    if answer2 == "c" or answer1 == "miti":
        score += 1
        print("Paki paki! Ka pai!")
        print("\n")
    else:
        print("Racist Pākehā, you're wrong. Stop colonising Aotearoa")
        print("Score: ", score)
        print("\n")

    # question 3
    answer3 = input("What is the Maori word for fruits? \na. huarākau \nb. hēki \nc. ika\n\n").lower()
    if answer3 == "a" or answer1 == "huarakau":
        score += 1
        print("Paki paki! Ka pai!")
        print("\n")
    else:
        print("Racist Pākehā, you're wrong. Stop colonising Aotearoa")
        print("Score: ", score)
        print("\n")

    # question 4
    answer4 = input("What is the Maori word for egg? \na. wai kokonati \nb. hēki \nc. kawhe\n\n").lower()
    if answer4 == "b" or answer1 == "heki":
        score += 1
        print("Paki paki! Ka pai!")
        print("\n")
    else:
        print("Racist Pākehā, you're wrong. Stop colonising Aotearoa.")
        print("Score: ", score)
        print("\n")

    # question 5
    answer5 = input("What is the Maori word for coffee? \na. kawhe \nb. hupa \nc. huamata\n\n").lower()
    if answer5 == "a" or answer1 == "kawhe":
        score += 1
        print("Paki paki! Ka pai!")
        print("\n")
    else:
        print(formatter("X", "Racist Pākehā, you're wrong. Stop colonising Aotearoa."))
        print("Score: ", score)
        print("\n")

    # final message
    if score <= 1:
        print("Your total score is:", score, "- Disgraceful.")
    elif score <= 3:
        print("Your total score is:", score, "- You did ok.")
    else:
        print("Your total score is:", score, "- 非常好。")

    play_again = input("\nDo you want to play another round?\n<enter> "
                       "to play "
                       "again or 'X' to exit").lower()
    if play_again = "<enter>":
        
