cases = int(input()) 

for _ in range(cases):
    total = 0 
    sequence = list(map(int, input().split())) 

    for idx, options in enumerate(sequence):
        if idx == 0:
            continue
        if idx == sequence[0]: 
            total += options
        else:
            total += options - 1 
    print(total)
