"""Using lists for the questions to make code more compact
"""


word_list = [["paraoa", "bread"], ["tīhi", "cheese"], ["ika", "fish"],
               ["huarākau", "fruits"], ["huamata", "salad"],
               ["mīti", "meat"], ["hupa", "soup"], ["kawhe", "coffee"],
               ["hēki", "egg"], ["wai kokonati", "coconut water"]]

answer1 = input(f"What is the Maori word for {word_list[0][1]}?: ")

if answer1 == word_list[0][0]:
    print("✓", "Paki paki! Ka pai!")
    print("\n")
else:
    print("X", "Wrong."
