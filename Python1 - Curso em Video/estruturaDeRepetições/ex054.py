year1, year2, year3, year4, year5, year6, year7 = map(int, input('Digite sete anos: ').split(' '))

myArr = [year1, year2, year3, year4, year5, year6, year7]
saoDeMaior = 0;
naoSaoDeMaior = 0;

for x in range(0, len(myArr)):
    if 2021 - myArr[x] >= 18:
        saoDeMaior += 1
    else:
        naoSaoDeMaior += 1
print('{} maior(es) e {} menor(es) de idade'.format(saoDeMaior, naoSaoDeMaior))