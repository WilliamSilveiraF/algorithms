def getKeys(arr):
    myKeys = []
    for n in arr:
        if not(n in myKeys):
            myKeys.append(n)
    return myKeys

while True:
    fakeTicket = 0
    truthTickets, people = input().split(' ')
    if truthTickets == '0' and people == '0':
        break
    tickets = input().split(' ')
    keyTickets = getKeys(tickets)
    for keyTicket in keyTickets:
        if tickets.count(keyTicket) > 1:
            fakeTicket += 1
    print(fakeTicket)