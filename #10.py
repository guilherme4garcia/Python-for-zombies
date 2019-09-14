cigarrosdia = int(input('Qual a quantidade de cigarros fumados por dia? '))
cigarrosano = int(input('Por quantos anos você fumou? '))
total = cigarrosdia * (cigarrosano * 365)
diasperdidos = (total * 10) / 1440
print(f'Dias perdidos de vida: {diasperdidos:.0f}')