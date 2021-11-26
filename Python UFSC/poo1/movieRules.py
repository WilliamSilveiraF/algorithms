ageA = int(input())
ageB = int(input())

if ageA < 6 or ageB < 6:
    print("NO") #se pelo menos um for menor que 6
elif ageA >= 18 or ageB >= 18:
    print("YES") #se pelo menos um for maior ou igual a 18
elif ageA >= 14 and ageB >= 14:
    print("YES")#se ambos forem igual ou maior do que 14
else:
    print("NO") #se não atender as demandas acima, não pode entrar