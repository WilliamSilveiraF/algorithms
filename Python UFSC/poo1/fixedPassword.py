valorVerdade = False

while valorVerdade == False:
    senha = int(input())
    if senha == 2002:
        print("Acesso Permitido")
        valorVerdade = True
    else:
        print("Senha Invalida")