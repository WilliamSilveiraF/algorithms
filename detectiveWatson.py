def scndBiggestNum(arr):
    arr = sorted(arr, reverse=True)
    return arr[1]

while True:
    selectedKiller = input()
    if selectedKiller == '0': break
    killers = list(map(int, input().split(' ')))
    print(killers.index(scndBiggestNum(killers)) + 1)
