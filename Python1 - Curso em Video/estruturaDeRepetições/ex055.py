myArr = list(map(int, input('Digite cinco pesos: ').split(' ')))
print(myArr)
pesoMaior = myArr[0];
pesoMenor = myArr[0];
for x in range(0, len(myArr)):
    if pesoMaior < myArr[x]:
        pesoMaior = myArr[x]
    if pesoMenor > myArr[x]:
        pesoMenor = myArr[x]
print('Maior Peso: {}\n'
      'Menor Peso: {}'.format(pesoMaior, pesoMenor))