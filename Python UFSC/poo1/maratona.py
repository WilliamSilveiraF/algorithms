waterStations, allowedDist = map(int, input().split(' '))
stationsPositions = list(map(int, input().split(' ')))

for x in range(1, waterStations):
    now = stationsPositions[x]
    before = stationsPositions[x - 1]
    if now - before > allowedDist:
        print('N')
        break
    if waterStations == x + 1:
        if 42195 - stationsPositions[waterStations - 1] > allowedDist:
            print('N')
        else:
            print('S')
