turns = int(input())
sequence = []
result = []
for turn in range(turns):
    theUnit = int(input())
    sequence.append(theUnit)
    result.append(0)
for idx, power in enumerate(sequence):
    if idx == 0 and power == 1:
        result[0] += 1
        result[1] += 1
    elif idx == len(sequence) - 1 and power == 1:
        result[-1] += 1
        result[idx - 1] += 1
    elif power == 1:
        result[idx] += 2
        if sequence[idx - 1] == 1 and sequence[idx + 1] == 1:
            result[idx] += 1
        if sequence[idx + 1] == 0:
            result[idx + 1] += 1
        if sequence[idx - 1] == 0:
            result[idx - 1] += 1
    print(f"Round: {idx}, {result}")

for x in result:
    print(x)
