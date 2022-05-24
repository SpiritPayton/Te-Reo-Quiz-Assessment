"""Final message to show the player their score v2
added 'out of 6' after the player's score and added a play again function"""
if score <= 2:
    print("Your total score is:", score, "out of 6 - Disgraceful.")
elif score <= 4:
    print("Your total score is:", score, "out of 6 - You did ok.")
else:
    print("Your total score is:", score, "out of 6 - 非常好！！！")

play_again = input("\nDo you want to play again to try get a higher score?\n<enter> "
                   "to play "
                   "again or 'X' to exit: ").upper()
