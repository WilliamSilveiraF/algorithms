turns = int(input())

carrinhos = 0
bonecas = 0

for turn in range(turns):
    childGender = input()[-1]
    if childGender == 'M':
        carrinhos += 1
    elif childGender:
        bonecas += 1
print(f"{carrinhos} carrinhos\n"
      f"{bonecas} bonecas")