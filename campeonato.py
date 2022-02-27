cv, ce, cs, fv, fe, fs = map(int, input().split(' '))
pontC = (cv * 3) + (ce * 1)
pontF = (fv * 3) + (fe * 1)

if (pontC > pontF) or (pontC == pontF and cs > fs):
    print('C')
elif pontF > pontC or (pontF == pontC and fs > cs):
    print('F')
else:
    print('=')