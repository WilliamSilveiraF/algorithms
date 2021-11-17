import random
numChosen = random.randint(0, 10)
myChoice = int(input('Qual é o seu palpite? '))
tentativas = 1
while numChosen != myChoice:
    tentativas += 1
    print('Tente novamente!')
    myChoice = int(input('Seu novo palpite: '))
print('Parabéns, você conseguiu com {} tentativas'.format(tentativas))