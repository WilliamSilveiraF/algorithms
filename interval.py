num = float(input())

if num >= 0 and 25.00 >= num:
    print('Intervalo [0,25]')
elif num > 25.00 and 50.00 >= num:
    print('Intervalo (25,50]')
elif num > 50.00 and 75.00 >= num:
    print('Intervalo (50,75]')
elif num > 75.00 and 100.00 >= num:
    print('Intervalo (75,100]')
else:
    print('Fora de intervalo')