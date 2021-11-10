myNum = int(input())
u = myNum // 1 % 10
d = myNum // 10 % 10
c = myNum // 100 % 10
m = myNum // 1000 % 10
print('unidade: {}\n'
      'dezena: {}\n'
      'centena: {}\n'
      'milhar: {}'.format(u, d, c, m))
