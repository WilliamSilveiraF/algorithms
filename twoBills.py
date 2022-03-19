bills = [100, 50, 20, 10, 5, 2] 

while True:
    isPossible = False 
    value, payment = map(int, input().split()) 

    if value == 0 and payment == 0: 
        break
    diff = payment - value 

    for idx, note in enumerate(bills):
        for nIdx, note2 in enumerate(bills):
            if nIdx <= idx:
                continue
            if note + note2 == diff: 
                isPossible = True 
                break
        if isPossible: 
            print("possible")
            break
    if not isPossible: 
        print("impossible")
