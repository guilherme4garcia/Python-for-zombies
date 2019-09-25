peso = float(input('Digite o peso dos peixes em quilogramas: '))

if peso > 50:
   excesso = peso - 50
   multa = excesso * 4

else:
    excesso = 0
    multa = 0

print(f'João Papo-de-Pescador excedeu {excesso} kg, o valor da multa será de R${multa:.2f}')