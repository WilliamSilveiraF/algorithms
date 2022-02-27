b = int(input())
t = int(input())

retangulo = 70 * 160
# trapezio = ((b + B) * h) / 2
# calculando o tamanho de cada um
felixSide = ((b + t) * 70) / 2
marziaSide = retangulo - felixSide
#Se felix maior, print 1
if felixSide > marziaSide:
    print("1")
#Se Marzia maior, print 2
elif felixSide < marziaSide:
    print("2")
#Se tudo igual, print 0
else:
    print("0")