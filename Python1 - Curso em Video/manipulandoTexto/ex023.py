myNum = str(input())
newList = myNum.replace('', ' ').strip().split(' ');
print('unidade: {}\n'
      'dezena: {}\n'
      'centena: {}\n'
      'milhar: {}'.format(newList[3], newList[2], newList[1], newList[0]))
