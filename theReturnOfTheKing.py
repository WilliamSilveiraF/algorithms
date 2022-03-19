nRunes, amtFriendship = map(int, input().split(' ')) #pegue a quantidade de runes e amizade
runes = {} #set meu dicionário de runas

for _ in range(nRunes): #percorre todas as quantidades de nRunes, para coletar todas as runas
    ri, vi = input().split() #pega runa e o valor da amizade
    runes[ri] = int(vi) #cadastra runa e seu respectivo valor no meu dicionário de runa

_ = input() #ignora a quantidade de runas recitadas por Frodo e Sam

selected = input().split(' ') #pega a lista de runas recitadas

framt = 0 #set meu índice de quantidade de amizade

for rune in selected: #conta todos os valores das minhas runas recitadas
    framt += runes[rune]

print(framt) #printa minha quantidade de amizade

if framt >= amtFriendship:
    print("You shall pass!")
else:
    print("My precioooous")