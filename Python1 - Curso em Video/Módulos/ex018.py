from math import sin, cos, tan

angulo = float(input('Digite um ângulo: '))
anguloEmRad = angulo * 3.14 / 180
mySeno = sin(anguloEmRad)
myCos = cos(anguloEmRad)
myTag = tan(anguloEmRad)
print('Meu seno é {:.2f}, meu cosseno é {:.2f} e minha tangente é {:.2f}'.format(mySeno, myCos, myTag))
