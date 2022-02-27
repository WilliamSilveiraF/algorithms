initValue, amtOperations = map(int, input().split(' '))
players = ['D', 'E', 'F']
bank = [initValue, initValue, initValue]  # order by D, E, F

def buy(buyer, price):
    buyer = players.index(buyer)
    bank[buyer] -= int(price)


def sell(seller, price):
    seller = players.index(seller)
    bank[seller] += int(price)

def rent(locator, tenant, price):
    locator = players.index(locator)
    tenant = players.index(tenant)
    bank[locator] += int(price)
    bank[tenant] -= int(price)

for nTurns in range(amtOperations):
    operation = input().split(' ')
    if len(operation) > 3:
        theType, locator, tenant, price = operation
        rent(locator, tenant, price)
    else:
        theType, player, price = operation
        buy(player, price) if theType == "C" else sell(player, price)
print(f"{bank[0]} {bank[1]} {bank[2]}")