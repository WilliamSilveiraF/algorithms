houseValue = float(input('Qual o valor da casa: '))
buyerIncome = float(input('Qual o salário mensal do comprador: '))
timeSizeYear = float(input('Tamanho do financiamento em anos:'))
answer = buyerIncome * 0.30 * 12 * timeSizeYear
if answer > houseValue:
    print('Parabéns! Empréstimo aprovado!')
else:
    print('Empréstimo negado!')
