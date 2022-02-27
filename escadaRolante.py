times = int(input())

historico = []
diferenca = 0
for time in range(times):
    instante = int(input())
    historico.append(instante)

for tempo in range(len(historico) - 1):
    diferenca += historico[tempo+1] - historico[tempo]
diferenca += 10
if times == 0:
    diferenca = 0
print(diferenca)