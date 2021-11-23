bolas = int(input())
braços = int(input())

if braços // 2 > bolas:
    qtd = (braços // 2) - bolas
    print(f"Faltam {qtd} bolinha(s)")
else:
    print("Amelia tem todas bolinhas!")