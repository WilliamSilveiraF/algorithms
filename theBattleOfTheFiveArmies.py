h, e, a, o, w, x = map(int, input().split(' ')) #separando por espaços e aplicando atirando valor int para todos os elementos
goodSide = h + e + a + x #calculando lado bom
evilSide = o + w #calculando lado ruim
if goodSide > evilSide: #se lado bom maior que lado ruim print: Middle-earth is safe.
    print("Middle-earth is safe.")
else: #De outra maneiro print: Sauron has returned.
    print("Sauron has returned.")