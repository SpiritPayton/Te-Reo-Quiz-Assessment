"""Function to display 4 words in Te Reo and 1 word in English,
the English word meaning the same as one of the Te Reo words.
(the code is mostly copied from someone online,
and it's not actually an interactive quiz yet)
"""

from random import shuffle, sample

# the answers
alt1 = """bread, paraoa
cheese, tīhi
fish, ika
fruits, huarākau
meat, mīti
soup, hupa
coffee, kawhe
egg, hēki
coconut water, wai kokonati"""

alt1 = alt1.splitlines()
qnum = len(alt1)

sol = alt1.copy()
questions = []
answers = []
for q in alt1:
	q, a = q.split(",")
	questions.append(q)
	answers.append(a)

qna = []
lettsol = []
letters = "abcd"
for n in range(qnum):
	a1 = sol[n].split(",")[1]
	pos = answers.index(a1)
	answers.pop(pos)
	shuffle(answers)
	a2, a3, a4 = sample(answers, 3)
	qq = f"What is the Maori word for {questions[n]}"
	x = [a1, a2, a3, a4]
	shuffle(x)
	right = x.index(a1)
	lettsol.append(letters[right])
	qna.append([qq, x])
	answers.insert(pos, a1)
# print(*qna, sep="\n")
counter = 0

for q in qna:
	q, a = q
	print(q)
	for ans in a:
		print(f"{letters[counter]})" + ans)
		counter += 1
	counter = 0
	print()


print("\nSolutions")
counter = 0
for ss in sol:
	q, s = ss.split(",")
	print(q, s, " [" + lettsol[counter] + "]")
	counter += 1
