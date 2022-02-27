def getPositions(theMax, arr):
    indexs = ''
    for idx, n in enumerate(arr):
        if n == theMax:
            indexs += ' ' + str(idx)
    return indexs.strip()

nTest = 1

while True:
    airportAmt, flightsAmt = map(int, input().split(' '))
    if airportAmt == 0 and flightsAmt == 0:
        break
    flights = [0] * (airportAmt + 1)

    for _ in range(1, flightsAmt + 1):
        departure, arrival = map(int, input().split(' '))
        flights[departure] += 1
        flights[arrival] += 1
    print(f"Teste {nTest}\n"
          f"{getPositions(max(flights), flights)}")
    nTest += 1
