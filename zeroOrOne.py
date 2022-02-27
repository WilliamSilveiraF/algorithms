while True:
    try:
        a, b, c = map(int, input().split(' '))
        if a != b and b == c:
            print('A')
            continue
        elif a != b and a == c:
            print('B')
            continue
        elif c != a and a == b:
            print('C')
            continue
        elif a == b ==c:
            print('*')
    except EOFError:
        break
