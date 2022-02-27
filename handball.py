scoreAllMatches = 0

playersAmt, matchesAmt = map(int, input().split())

for _ in range(playersAmt):
    match = list(map(int, input().split()))

    if not(0 in match):
        scoreAllMatches += 1

print(scoreAllMatches)
