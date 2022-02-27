amtParts = int(input())
iHave = list(map(int, input().split()))

parts = [0] * (amtParts + 1)

for part in iHave:
    parts[part] = 1

for idx in range(1, len(parts)):
    if parts[idx] == 0:
        print(idx)
        break
