import math

arrNotas = [100.00, 50.00, 20.00, 10.00, 5.00, 2.00]
arrMoedas = [1.00, 0.50, 0.25, 0.10, 0.05, 0.01]

valor = float(input())
print('NOTAS:')
for notaAtual in arrNotas:
    (qtdRemovida, newValor) = divmod(valor, notaAtual)
    valor = newValor
    print('{:.0f} nota(s) de R$ {:.2f}'.format(qtdRemovida, notaAtual))
print('MOEDAS:')
for moedaAtual in arrMoedas:
    (qtdRemovida, newValor) = divmod(valor*100, moedaAtual*100)
    valor = newValor / 100
    print('{:.0f} moeda(s) de R$ {:.2f}'.format(qtdRemovida, moedaAtual))