questionsNumber = int(input())
desafortunatoAnswers = input()

classmatesAmt = int(input())
classmatesAnswers = []

for _ in range(classmatesAmt):
    classmateAnswer = input()
    classmatesAnswers.append(classmateAnswer)
answersByQuestion = []
for question in range(questionsNumber):
    desafortunatoAnswer = desafortunatoAnswers[question]
    answerForTheQuestion = ''
    for answer in classmatesAnswers:
        classmateAnswer = answer[question]
        if desafortunatoAnswer != classmateAnswer:
            answerForTheQuestion += classmateAnswer
    answersByQuestion.append(answerForTheQuestion)

result = 0

for answers in answersByQuestion:
    if answers == '':
        continue
    counter = 0
    mostFrequent = answers[0]
    for letter in answers:
        curr_frequency = answers.count(letter)
        if curr_frequency > counter:
            counter = curr_frequency
            mostFrequent = letter
    result += answers.count(mostFrequent)

print(result)
