cases = int(input())

arr = []
for _ in range(cases):
    arr.append(int(input()))

diffStickers = len(set(arr))

countRepeated = 0
for n in (set(arr)):
    if arr.count(n) > 1:
        countRepeated += arr.count(n) - 1

print(diffStickers)
print(countRepeated)