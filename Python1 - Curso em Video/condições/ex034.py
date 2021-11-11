salario = float(input('Qual é o seu salário? '))

if salario > 1250.00:
    newSalario = salario * 1.10
else:
    newSalario = salario * 1.15
print('Seu novo salário é {:.2f}'.format(newSalario))