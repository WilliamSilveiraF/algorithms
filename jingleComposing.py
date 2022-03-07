notes = {'W': 1.0, 'H': 0.5, 'Q': 0.25, 'E': 0.125, 'S': 0.0625, 'T': 0.03125, 'X': 0.015625}

while True:
    result = 0
    sequence = input().split("/")

    if sequence[0]:
        break

    for note in sequence:
        t = 0
        for part in note:
            t += notes[part]
        if t == 1.0:
            result += 1
    print(result)