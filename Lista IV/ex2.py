# Sorteie 20 inteiros entre 1 e 100 numa lista. Armazene os números pares na lista PAR e os
# números ímpares na lista IMPAR. Imprima as três listas.

from random import randint

lista = []
par = []
impar = []

for c in range(0, 20):
    lista.append(randint(1, 100))
    if lista[c] % 2 == 0:
        par.append(lista[c])
    else:
        impar.append(lista[c])

print(f'Lista Par: {par}')
print(f'Lista Ímpar: {impar}')
print(f'Lista Completa: {lista}')
