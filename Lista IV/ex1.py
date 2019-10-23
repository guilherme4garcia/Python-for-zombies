# Sorteie 10 inteiros entre 1 e 100 para uma lista e descubra o maior e o menor valor, sem usar
# as funções max e min

from random import randint

lista = []
maior = 1
menor = 100

for c in range(0, 10):
    n = randint(1, 100)
    lista.append(n)

c = 0

for c in range(0, 10):
    if lista[c] < menor:
        menor = lista[c]

    if lista[c] > maior:
        maior = lista[c]

print(lista)
print(f'Maior valor: {maior}')
print(f'Menor valor: {menor}')


