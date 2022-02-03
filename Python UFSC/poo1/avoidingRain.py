turns = int(input())

homeBuyed = 0
officeBuyed = 0
homeStock = 0
officeStock = 0

for _ in range(turns):
    sd, sn = input().split(' ')

    if sd == 'chuva':
        if homeStock > 0:
            officeStock += 1
            homeStock -= 1
        else:
            homeBuyed += 1
            officeStock += 1

    if sn == 'chuva':
        if officeStock > 0:
            officeStock -= 1
            homeStock += 1
        else:
            officeBuyed += 1
            homeStock += 1

print(f"{homeBuyed} {officeBuyed}")

