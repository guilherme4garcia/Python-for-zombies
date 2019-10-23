# Verifique se um inteiro positivo n é primo

#se o % = 0 não é primo

n = int(input('Digite um número inteiro positivo para saber se é primo: '))
total = 0
for c in range(1, n + 1):
    if n % c == 0:
        total += 1

if total == 2:
    print(f'O número {n} foi divisível {total} vezes. Ele é primo')

else:
    print(f'O número {n} foi divisível {total} vezes. Ele não é primo.')