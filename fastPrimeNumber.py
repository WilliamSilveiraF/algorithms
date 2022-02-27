from math import sqrt
vezes = int(input())
for vez in range(0, vezes):
    myNum = int(input())
    valorVerdade = True

    if myNum % 2 == 0:
        valorVerdade = False
    else:
        for impar in range(3, int(sqrt(myNum))+1, 2):
            if myNum % impar == 0:
                valorVerdade = False
                break

    if valorVerdade or myNum == 2:
        print('Prime')
    else:
        print('Not Prime')