day1, month1 = map(int, input().split(' '))
day2, month2 = map(int, input().split(' '))
diasDosMes = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
amountDays1 = 0
amountDays2 = 0

for n in range(1, 12):
    if month1 > n:
        amountDays1 += diasDosMes[n - 1]

for x in range(1, 12):
    if month2 > x:
        amountDays2 += diasDosMes[x - 1]

amountDays1 += day1
amountDays2 += day2
if amountDays1 > amountDays2:
    print(amountDays1 - amountDays2)
else:
    print(amountDays2 - amountDays1)
