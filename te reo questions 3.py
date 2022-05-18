"""function to ask the quiz questions AND display score at end
no randomisation of questions & answers yet
"""


class Question:
    def __init__(self, prompt, answer):
        self.prompt = prompt
        self.answer = answer


question_prompts = [
    "What is the Maori word for bread? \na. paraoa \nb. ika \nc. hupa\n\n",
    "What is the Maori word for meat? \na. kawhe \nb. huamata \nc. mīti\n\n",
    "What is the Maori word for fruits? \na. huarākau \nb. hēki \nc. ika\n\n"]


# ignore this
"""bread" = "paraoa"
"cheese" = "tīhi"
"fish" = "ika"
"fruits" = "huarākau"
"salad" = "huamata"
"meat" = "mīti"
"soup" = "hupa"
"coffee" = "kawhe"
"egg" == "hēki"
"coconut water" = "wai kokonati"""


questions = [
    Question(question_prompts[0], "a"),
    Question(question_prompts[1], "c"),
    Question(question_prompts[2], "a")]


def run_test(questions):
    score = 0
    for question in questions:
        answer = input(question.prompt)
        if answer == question.answer:
            score += 1
    print("You got " + str(score) + "/" + str(len(questions)) + " Correct")


run_test(questions)
