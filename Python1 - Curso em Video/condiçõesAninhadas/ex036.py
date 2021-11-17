houseValue = float(input('Qual o valor da casa: '))
buyerIncome = float(input('Qual o salário mensal do comprador: '))
timeSizeYear = float(input('Tamanho do financiamento em anos:'))
answer = buyerIncome * 0.30 * 12 * timeSizeYear
parcela = houseValue / (timeSizeYear * 12)
if answer > houseValue:
    print('Parabéns! Empréstimo aprovado com parcela fixa no valor de R$ {:.2f} mensais!'.format(parcela))
else:
    print('Empréstimo negado!')
