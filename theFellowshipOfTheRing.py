char = {'A': 0, 'E': 0, 'H': 0, 'M': 0, 'X': 0}

case = int(input())

for _ in range(case):
    test = input().split()
    char[test[1]] += 1

print(f"{char['X']} Hobbit(s)"
      f"\n{char['H']} Humano(s)"
      f"\n{char['E']} Elfo(s)"
      f"\n{char['A']} Anao(s)"
      f"\n{char['M']} Mago(s)"
)