from math import ceil #importando lib para arredondar pro auto
valor = int(input())
numeroParcelas = int(input())


while valor > 0: #calcula parcelas até o valor zera
    if valor % numeroParcelas != 0: #se não for multiplo do número de parcelas, é dividido e arrendondado pro alto
        removido = ceil(valor / numeroParcelas)
    else: #se for multiplo é removido o valor inteiro da divisão do valor pelo num de parcelas
        removido = valor / numeroParcelas
    valor -= removido
    numeroParcelas -= 1
    print(int(removido))