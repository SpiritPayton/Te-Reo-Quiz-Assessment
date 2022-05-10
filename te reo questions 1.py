"""Function to display 4 words in Te Reo and 1 word in English,
the English word meaning the same as one of the Te Reo words.
"""


# answers (I'm not yet exactly sure how to make them mean the same thing)
"bread" == "paraoa"
"cheese" == "tīhi"
"fish" == "ika"
"fruits" == "huarākau"
"salad" == "huamata"
"meat" == "mīti"
"soup" == "hupa"
"coffee" == "kawhe"
"egg" == "hēki"
"coconut water" == "wai kokonati"

english_word = 0
maori_word = 0


# asking the questions and getting input (Not good though)
while True:
    d1a = input("Maori words: \n A) [maori word 1]. B) [maori word 2]. [A/B]? : ").lower()
    if d1a == "a":
        print("next question")
    elif d1a == "b":
        print("wrong. next question")
        break


# Main routine goes here
