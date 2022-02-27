n, m = map(int, input().split(' '))#Peguei meus nums

p1 = n #mudei as variaveis para entendimento melhor
p2 = m

def eh_Primo(num): #função que retorna booleano se meu número é primo ou não 
    for x in range(num, 0, -1):
        if num % x == 0 and x != 1 and x != num: #Se ele for divisível por um número diferente de 1 e ele mesmo, ele não é primo
            return False
        elif x == 1:
            return True

while p1 > 0: 
    if eh_Primo(p1):#Loops caçando o primo mais próximo, no primeiro primo que achar, o loop para
        break
    p1 -= 1
while p2 > 0:
    if eh_Primo(p2):
        break
    p2 -= 1
print(p1 * p2) #multiplicando
