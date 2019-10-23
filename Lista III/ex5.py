print('MDC - Algoritmo de Euclides')
a = int(input('Digite um número inteiro positivo: '))
b = int(input('Digite um segundo número inteiro positivo: '))
r = 0

while a <= 0 or b <= 0:
    print('Os números devem ser positivos.')
    a = int(input('Digite um número inteiro positivo: '))
    b = int(input('Digite o segundo número inteiro positivo: '))

while b != 0:
    r = a % b
    a = b
    b = r

print(f'O máximo divisor comum entre eles é: {a}')
