turns = int(input())

minas = [0] * turns

for i in range(0, turns):
    bomb = int(input())

    left = i - 1
    right = i + 1

    minas[i] += bomb
    if left >= 0:
        minas[left] += bomb
    if right <= turns - 1:
        minas[right] += bomb

for result in range(0, turns):
    print(minas[result])
