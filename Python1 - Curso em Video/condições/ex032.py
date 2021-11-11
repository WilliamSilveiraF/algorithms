from datetime import date
year = int(input())
if year == 0:
    year = date.today().year
if year % 4 == 0 and year % 100 != 0:
    print('É bissexto')
else:
    print('Não é bissexto')
