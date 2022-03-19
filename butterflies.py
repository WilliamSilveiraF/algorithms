rows = int(input()) #pegue minhas linhas para formar minha matriz de borboletas

butterflies = [] #armazenar as espécies de borboletas que Bino achou
matrix = [] #armazena todas as espécies de borboletas
for _ in range(rows): #formato minha matriz em um array
    row = list(map(int, input().split(' ')))
    matrix.append(row)

for _ in range(rows * 2): #conforme o enuciado, bino captura rows * 2 borboletas
    x, y = list(map(int, input().split(' '))) #pego a coordenada
    x -= 1 #reduzo -1, pois os índices no python começam em zero
    y -= 1
    for idx, row in enumerate(matrix): #procure a coordenada onde binho capturou a borboleta e armazene sua espécie
        if idx == x:
            for yIdx, butterfly in enumerate(matrix[idx]):
                if yIdx == y:
                    butterflies.append(butterfly)

print(len(set(butterflies))) #com set pegue a lista de espécie sem repetição e ache a quantidade de espécies achadas por bino com o length