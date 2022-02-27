otavio, bruno, ian = map(float, input().split(' '))

if otavio < bruno and otavio < ian:
    print("Otavio")
elif bruno < otavio and bruno < ian:
    print("Bruno")
elif ian < otavio and ian < bruno:
    print("Ian")
else:
    print("Empate")