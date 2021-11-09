A, B, C = list(map(int, input().split(' ')))
X, Y, Z = list(map(int, input().split(' ')))

contPorAltura = Z // C
contPorComprimento = Y // B
contPorLargura = X // A

volumeMax = contPorLargura * contPorComprimento * contPorAltura
print('{:.0f}'.format(volumeMax))
