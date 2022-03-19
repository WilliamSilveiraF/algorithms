while True:
    try:
        numbers = {}  
        mostFrequent = (-1, -1) 
        sequence = input() 
        for n in sequence: 
            if n not in numbers.keys(): 
                numbers[n] = 1
            else: 
                numbers[n] += 1
        for key, value in numbers.items(): 
            mfKey, mfValue = mostFrequent 
            if value == mfValue: 
                if int(key) > int(mfKey):
                    mostFrequent = (key, value)
            elif value > mfValue: 
                mostFrequent = (key, value)
        print(mostFrequent[0]) 
    except EOFError:
        break;
