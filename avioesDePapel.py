competidores, qtdFolhas, razaoDeFolhas = map(int, input().split())

if competidores * razaoDeFolhas <= qtdFolhas:
    print('S')
else:
    print('N')