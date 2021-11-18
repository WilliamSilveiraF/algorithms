vezes = int(input())

for x in range(vezes):
    face3 = int(input())
    face1, face2, face6, face5 = map(int, input().split(' '))
    face4 = int(input())
    dado = [face1, face2, face3, face4, face5, face6]
    if face1 + face6 == 7 and face2 + face5 == 7 and face3 + face4 == 7 and sorted(dado) == [1, 2, 3, 4, 5, 6]:
        print("SIM")
    else:
        print("NAO")