troopA = 0
troopB = 0

length, width, soldiersAmt = map(int, input().split())

angularIndex = length / width

for soldier in range(soldiersAmt):
    x, y, skill = map(int, input().split())
    if y * angularIndex > x:
        troopA += skill
    else:
        troopB += skill
print(f"{troopA} {troopB}")
