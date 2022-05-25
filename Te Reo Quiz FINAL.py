"""Te Reo foods quiz FINAL, PEP8 checked
added goodbye message as a final touch
"""


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
    print("I'm going to give you 3 names of food in Te Reo,")
    print("and the name of a food in English.")
    print()
    print("The English word will mean the same food as "
          "one of the Te Reo words.")
    print("You will need to select which word you think"
          " (or hopefully know) it is.")
    print("There will be 6 rounds of questions. "
          "Good luck, and kia kaha.")
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
print(formatter("-", "Kia ora! Are you ready to test"
                     " your Te Reo Māori skills?"))
print()

print("You're about to learn how to say some"
      " kai names in Māori.")
print()
played_before = yes_no("Have you played this game"
                       " before?: ").lower()
print()

if played_before == "no":
    instructions()

rounds_played = 0

# begin game - question 1
while play_again != "X":  # while loop to play the quiz again or exit
    score = 0  # reset the score to 0
    rounds_played += 1  # keep track of rounds
    print(formatter(".", f"Round {rounds_played}"))
    print()
    print("-QUESTION 1-")
    answer1 = input("What is the Maori word for bread?"
                    " \na. paraoa \nb. ika \nc. hupa\n\n").lower()
    if answer1 == "a" or answer1 == "paraoa":
        score += 1
        print(formatter("✓", "Paki paki! Ka pai!"))
        print("\n")
    else:
        print(formatter("X", "Racist Pākehā, you're wrong."
                             " Stop colonising Aotearoa."))
        print("Score: ", score)
        print("\n")

    # question 2
    print("QUESTION 2")
    print()
    answer2 = input("What is the Maori word for meat?"
                    " \na. kawhe \nb. huamata \nc. mīti\n\n").lower()
    if answer2 == "c" or answer2 == "miti":
        score += 1
        print(formatter("✓", "Paki paki! Ka pai!"))
        print("\n")
    else:
        print(formatter("X", "Racist Pākehā, you're wrong."
                             " Stop colonising Aotearoa"))
        print("Score: ", score)
        print("\n")

    # question 3
    print("QUESTION 3")
    answer3 = input("What is the Maori word for fruits?"
                    " \na. huarākau \nb. hēki \nc. ika\n\n").lower()
    if answer3 == "a" or answer3 == "huarakau":
        score += 1
        print(formatter("✓", "Paki paki! Ka pai!"))
        print("\n")
    else:
        print(formatter("X", "Racist Pākehā, you're wrong."
                             " Stop colonising Aotearoa"))
        print("Score: ", score)
        print("\n")

    # question 4
    print("QUESTION 4")
    answer4 = input("What is the Maori word for egg?"
                    " \na. wai kokonati \nb. hēki \nc. kawhe\n\n").lower()
    if answer4 == "b" or answer4 == "heki":
        score += 1
        print(formatter("✓", "Paki paki! Ka pai!"))
        print("\n")
    else:
        print(formatter("X", "Racist Pākehā, you're wrong."
                             " Stop colonising Aotearoa."))
        print("Score: ", score)
        print("\n")

    # question 5
    print("QUESTION 5")
    answer5 = input("What is the Maori word for coffee?"
                    " \na. kawhe \nb. hupa \nc. huamata\n\n").lower()
    if answer5 == "a" or answer5 == "kawhe":
        score += 1
        print(formatter("✓", "Paki paki! Ka pai!"))
        print("\n")
    else:
        print(formatter("X", "Racist Pākehā, you're wrong."
                             " Stop colonising Aotearoa."))
        print("Score: ", score)
        print("\n")

    # question 6
    print("QUESTION 6")
    answer6 = input("What is the Maori word for coconut water?"
                    " \na. huamata \nb. aporo wai \nc. "
                    "wai kokonati\n\n").lower()
    if answer6 == "c" or answer6 == "wai kokonati":
        score += 1
        print(formatter("✓", "Paki paki! Ka pai!"))
        print("\n")
    else:
        print(formatter("X", "Racist Pākehā, you're wrong."
                             " Stop colonising Aotearoa."))
        print("Score: ", score)
        print("\n")

    # final message
    if score <= 2:
        print("Your total score is:", score, "out of 6 - Disgraceful.")
    elif score <= 4:
        print("Your total score is:", score, "out of 6 - You did ok.")
    else:
        print("Your total score is:", score, "out of 6 - 非常好！！！")

    play_again = input("\nDo you want to play again to "
                       "try get a higher score?\n<enter> to play "
                       "again or 'X' to exit: ").upper()

print()
print(formatter("*", "Ka kite anō!"))
