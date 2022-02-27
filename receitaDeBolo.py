a, b, c = map(int, input().split(' '))
#Ingredientes necessários para fazer uma receita completa
qtdIgnorandoOutros = [a // 2, b // 3, c // 5]
#O menor valor de ingredientes é também a máxima quantidade que eu consigo fazer de uma receita sem improviso
print(min(qtdIgnorandoOutros))