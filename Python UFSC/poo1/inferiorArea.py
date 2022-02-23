choice = input()
matrix = [None] * 12
result = 0

for line in range(12): # Para cada linha, atribua 12 colunas
    matrix[line] = [None] * 12

for line in range(12): #Recolha todos os valores dos inputs e coloque na linha e coluna correta
    for column in range(12):
        matrix[line][column] = float(input())

for line in range(7, 12): #some todos os elementos no meu intervalo de linha e coluna do meu enuciado
    for column in range(12 - line, line):
        result = result + matrix[line][column]
if choice == "M": #Se escolheu a média, divida por 30 (a quantidade do intervalo de coluna e linhas solicitado no enuciado)
        result = result / 30

print(f"{result:.1f}") #formate com uma casa decimal
