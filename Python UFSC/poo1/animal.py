tipo = str(input())
classe = str(input())
alimentacao = str(input())

if tipo == "vertebrado":
    if classe == "ave":
        if alimentacao == "carnivoro":
            print('aguia')
        if alimentacao == "onivoro":
            print('pomba')
    if classe == "mamifero":
        if alimentacao == "onivoro":
            print('homem')
        if alimentacao == "herbivoro":
            print('vaca')

if tipo == 'invertebrado':
    if classe == "inseto":
        if alimentacao == "hematofogo":
            print('pulga')
        if alimentacao == "herbivoro":
            print('lagarta')
    if classe == "anelideo":
        if alimentacao == "hematofogo":
            print('sanguessuga')
        if alimentacao == "onivoro":
            print('minhoca')