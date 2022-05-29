"""A more simple version of asking the questions.
no randomisation of questions or answers"""


# ignore this
"""bread" = "paraoa"
"cheese" = "tīhi"
"fish" = "ika"
"fruits" = "huarākau"
"salad" = "huamata"
"meat" = "mīti"
"soup" = "hupa"
"coffee" = "kawhe"
"egg" = "hēki"
"coconut water" = "wai kokonati"""


score = 0

# question 1
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
    print("Racist Pākehā, you're wrong. Stop colonising Aotearoa.")
    print("Score: ", score)
    print("\n")


# final message
if score <= 1:
    print("Your total score is:", score, "- Disgraceful.")
elif score <= 3:
    print("Your total score is:", score, "- You did ok.")
else:
    print("Your total score is:", score, "- 非常好。")
