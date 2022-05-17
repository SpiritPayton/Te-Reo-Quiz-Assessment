"""function to ask the quiz questions AND track score
"""


class Question:
    def __init__(self, prompt, answer):
        self.prompt = prompt
        self.answer = answer


question_prompts = [
    "What is the Maori word for bread? \na. paraoa \nb. ika \nc. hupa\n\n",
    "What is the Maori word for bread? \na. paraoa \nb. ika \nc. hupa\n\n",
    "What is the Maori word for bread? \na. paraoa \nb. ika \nc. hupa\n\n"]

questions = [
    Question(question_prompts[0], "a"),
    Question(question_prompts[1], "c"),
    Question(question_prompts[3], "b")]


def run_test(questions):
    score = 0
    for question in questions:
        answer = input(question.prompt)
        if answer == question.answer:
            score += 1
    print("You got " + str(score) + "/" + str(len(questions)) + "Correct")


run_test(questions)
