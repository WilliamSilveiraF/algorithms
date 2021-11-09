timeTotalSecond = int(input())
hora = timeTotalSecond // 3600
timeTotalSecond = timeTotalSecond - (hora * 3600)
minuto = timeTotalSecond // 60
timeTotalSecond = timeTotalSecond - (minuto * 60)
segundo = timeTotalSecond
print('{}:{}:{}'.format(hora, minuto, segundo))
