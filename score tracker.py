"""function to track the number of questions answered correctly
"""

answer1 = input("What is the Maori word for bread? \na. paraoa \nb. ika \nc. hupa \nAnswer: ").lower()
if answer == "a" or answer1 == "paraoa":
    score += 1
    print("Correct! Ka pai paki paki")
    print("Score: ", score)
    print("\n")
elif answer1 != "a" or answer1 != "paraoa":
    print("Wrong! The answer is paraoa")
    print("Score: ", score)
    print("\n")
else: 
