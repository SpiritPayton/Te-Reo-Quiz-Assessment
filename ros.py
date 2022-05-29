import random

score = 0
incorrect_answers = 0

q_list = [["question 1: 'Agnamar'. Please enter your answer: ",
"question"], ["question 2: 'Coterump'. Please enter your answer: ",
"computer"], ["question 3: Certcor. Please enter your answer: ", "correct"],
["question 4: Bleat. Please enter your answer: ", "table"]]


for i in range(0, len(q_list)):
    answer = input(q_list[i][0])
    if answer == q_list[i][1]:
        print("Correct!")
        score += 1
    else:
        incorrect_answers += 1
        print("Let's try again")
        continue

print("Your final score is: ", score)
