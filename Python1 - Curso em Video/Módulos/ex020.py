from random import shuffle

n1, n2, n3, n4 = list(input().split(' '))
list = [n1, n2, n3, n4]
shuffle(list)
print('A ordem de apresentação será {}'.format(list))
