times = int(input())
planejamento = 0
gastos = 0
for vez in range(times):
    action, value = input().split(' ')
    action = str(action)
    value = int(value)
    if action == "G":
        gastos += value
    elif action == "V":
        planejamento += value
if gastos > planejamento:
    print("NO CUT, FIGHT!")
else:
    print("A greve vai parar.")