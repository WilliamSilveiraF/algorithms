times = int(input())
planejamento = 0 #verba de planejamento
gastos = 0 #verba de gastos
for vez in range(times):
    action, value = input().split(' ') #coletando minha ação tipo caractere e meu valor
    action = str(action)
    value = int(value)
    if action == "G": #Se ação é gastar então soma aos gastos
        gastos += value
    elif action == "V": #Se ação foi ganhar orçamento então soma no planejamento
        planejamento += value
if gastos > planejamento:
    print("NAO VAI TER CORTE, VAI TER LUTA!") #Se meu gastos for maior que meu orçamento planejado não vai ter corte, vai ter luta
else:
    print("A greve vai parar.") #De outra maneira a greve para