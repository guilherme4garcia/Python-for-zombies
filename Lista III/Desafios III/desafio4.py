# Dado um número inteiro positivo, determine a sua decomposição em fatores primos
# calculando também a multiplicidade de cada fator

n = int(input('Digite um número inteiro positivo: '))

for c in range(2, n):

    while n % c == 0:
        print(c)
        n = n / c
