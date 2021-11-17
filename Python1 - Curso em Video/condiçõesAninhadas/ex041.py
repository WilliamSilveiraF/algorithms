idade = int(input('Digite sua idade: '))

if idade < 9:
    valorVerdade = 'MIRIM'
elif idade < 14:
    valorVerdade = 'INFANTIL'
elif idade < 19:
    valorVerdade = 'JUNIOR'
elif idade < 20:
    valorVerdade = 'SÊNIOR'
else:
    valorVerdade = 'MASTER'
print(valorVerdade)