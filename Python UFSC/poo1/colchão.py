a, b, c = map(int, input().split(' '))
h, l = map(int, input().split(' '))
minSize = h * l

if minSize >= a * b or minSize >= a * c or minSize >= b * c:
    if (a < h and b < l) or (b < h and a < l) or (b < h and c < l) or (c < h and b < l) or (a < h and c < l) or (
            c < h and a < l):
        print('S')
    else:
        print('N')
else:
    print('N')
