bolas = int(input())
braços = int(input())
#Se metade da divisão de inteira de braços for maior que a quantidade de bolas, calcule a quantidade que falta
if braços // 2 > bolas:
    
    qtd = (braços // 2) - bolas
    print(f"Faltam {qtd} bolinha(s)")
else:
    print("Amelia tem todas bolinhas!")