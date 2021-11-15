print('\033[31mEm vermelho!')
print('\033[1;31;43mEm vermelho com fundo amarelo!\033[m')
print('\033[4;97;45mLetra branca, fundo rosa e sublinhado!\033[m')
a = 3
b = 5
print('Os valores são \033[32m{}\033[m e \033[31m{}\033[m!!!'.format(a, b))

nome = 'William'
print('Olá! Muito prazer em te conhecer, {}{}{}!!'.format('\033[4;34m', nome, '\033[m'))

'''
text                    background
30   black        preto      40
31   red          vermelho   41
32   green        verde      42
33   yellow       amarelo    43
34   blue         azul       44
35   Magenta      Magenta    45
36   cyan         ciano      46
37   grey         cinza      47
97   white        branco     107
'''