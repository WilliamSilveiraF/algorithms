algo = input('Digite algo: ')
n1 = int(input('Digite um valor: '))
n2 = int(input('Digite outro: '))
s = n1 + n2
print(type(n1))

# print('A soma entre ', n1, 'e', n2, 'vale ', s)
print('A soma entre {0} e {1} vale {2}'.format(n1, n2, s))
print('A soma vale {0}, sendo de tipo {1}'.format(s, type(s)))

print(algo.isnumeric())
