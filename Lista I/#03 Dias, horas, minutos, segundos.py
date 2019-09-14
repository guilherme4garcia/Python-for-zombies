dias = int(input('Digite uma quantidade de dias: '))
horas = float(input('Digite uma quantidade de horas: '))
minutos = float(input('Digite uma quantidade de minutos: '))
segundos = float(input('Digite uma quantidade de segundos: '))

total = (dias * 86400) + (horas * 3600) + (minutos * 60) + segundos

print(f'{dias} dias, {horas:.2f} horas, {minutos:.2f} minutos e {segundos:.2f} segundos, equivale a {total:.2f} segundos.')
