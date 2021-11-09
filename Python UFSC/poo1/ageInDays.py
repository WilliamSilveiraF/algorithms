days = int(input())
ano = days // 365
mes = (days % 365) // 30
dia = (days % 365) - (mes * 30)
print('{} ano(s)\n'
      '{} mes(es)\n'
      '{} dia(s)'.format(ano, mes, dia))
