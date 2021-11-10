word = input().lower()
howManyTimes = word.count('a')
firstTime = word.find('a')
lastTime = word.find('a', -1)
print('Números de vezes: {}\n'
      'Primeira vez: {}\n'
      'Última vez: {}'.format(howManyTimes,
                              firstTime,
                              lastTime))
