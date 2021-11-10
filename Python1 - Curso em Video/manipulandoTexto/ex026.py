word = input().lower().strip()
howManyTimes = word.count('a')
firstTime = word.find('a')+1
lastTime = word.rfind('a')+1
print('Números de vezes: {}\n'
      'Primeira vez: {}\n'
      'Última vez: {}'.format(howManyTimes,
                              firstTime,
                              lastTime))
