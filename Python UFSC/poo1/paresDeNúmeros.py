n, i, f = input().split()
vector = input().split()

pairs = 0
idx = 0
for x in vector:
    for y in range(idx + 1, len(vector)):
        if int(i) <= (int(x) + int(vector[y])) <= int(f):
            pairs += 1
    idx += 1
print(pairs)
