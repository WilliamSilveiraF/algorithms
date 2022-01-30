turns = int(input())
sequence = []

homeBuyed = 0
officeBuyed = 0
homeStock = 0
officeStock = 0

def isHome(num):
    return num % 2 == 0

def isOffice(num):
    return not(num % 2 == 0)

for turn in range(turns):
    sd, sn = input().split(' ')
    sequence.append(sd)
    sequence.append(sn)

for index, weather in enumerate(sequence):
    if index == 0: continue

    if weather == 'chuva' and sequence[index - 1] == 'sol':
        if isHome(index):
            if homeStock > 0:
                officeStock += 1
                homeStock -= 1
            else:
                homeBuyed += 1
                officeStock += 1
        if isOffice(index):
            if officeStock > 0: #If i am in the office and win one umbrella, my home stock adds one umbrella
                homeStock += 1
                officeStock -= 1
            else:
                homeStock += 1
                officeBuyed += 1

print(f"{homeBuyed} {officeBuyed}")
