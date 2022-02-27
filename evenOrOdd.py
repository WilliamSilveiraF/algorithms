for i in range(int(input())):
    num = int(input())
    if num == 0:
        print('NULL')
    elif num > 0:
        if num % 2 == 0:
            print('EVEN POSITIVE')
        else:
            print('ODD POSITIVE')
    elif num < 0:
        if num % 2 == 0:
            print('EVEN NEGATIVE')
        else:
            print('ODD NEGATIVE')