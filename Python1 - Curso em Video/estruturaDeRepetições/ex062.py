initNum, ratio = map(int, input().split(' '))
x = 0
while x < 10:
    initNum += ratio
    print(initNum)
    x += 1
choice = (str(input('Quer mostrar mais algum termo? ')).upper())

if choice == 'S':
    quantosTermos = int(input('Quantos novos termos?'))
    while x < quantosTermos + 10:
        initNum += ratio
        print(initNum)
        x += 1