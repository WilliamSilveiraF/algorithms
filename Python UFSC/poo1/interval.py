num = float(input())
if num < 0 and num > 100.00:
    print('Fora de intervalo')
if num >= 0 and 25.00 >= num:
    print('Intervalo [0,25]')
if num > 25.00 and 50.00 >= num:
    print('Intervalo (25,50]')
if num > 50.00 and 75.00 >= num:
    print('Intervalo (50,75]')
if num > 75.00 and 100.00 >= num:
    print('Intervalo (75,100]')
