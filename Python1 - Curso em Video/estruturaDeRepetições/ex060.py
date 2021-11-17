number = int(input('Digite um número: '))
coeficiente = 1
while number != 0:
    coeficiente *= number
    print(number)
    number -= 1
print(coeficiente)