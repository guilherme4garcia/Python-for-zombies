distancia = float(input('Qual a distância percorrida em km: '))
dias = float(input('Qual a quantidade de dias que o carro foi alugado: '))
valordias = 60.00 * dias
valordistancia = 0.15 * distancia
total = valordias + valordistancia
print(f'R${total:.2f}')
