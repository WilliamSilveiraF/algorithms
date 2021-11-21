nSensorReadings, maximumCapacity = map(int, input().split(' '))
historia = []
qtd = 0
for n in range(nSensorReadings):
    saiu, entrou = map(int, input().split(' '))
    qtd -= saiu
    qtd += entrou
    historia.append(qtd)
if max(historia) > maximumCapacity:
    print("S")
else:
    print("N")