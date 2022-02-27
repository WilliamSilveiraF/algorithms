n1, n2, n3, n4 = list(map(float, input().split(' ')))
media = ((n1 * 2) + (n2 * 3) + (n3 * 4) + (n4 * 1)) / 10
print('Media: {:.1f}'.format(media))
if media >= 7.0:
    print('Aluno aprovado.')
if media < 5.0:
    print('Aluno reprovado.')
if media >= 5.0 and media < 7.0:
    print('Aluno em exame.')
    nExame = float(input())
    newMedia = (media + nExame) / 2
    print('Nota do exame: {:.1f}'. format(nExame))
    if newMedia >= 5.0:
        print('Aluno aprovado.')
    else:
        print('Aluno reprovado.')
    print('Media final: {}'.format(newMedia))