n1 = int(input('Digite uma nota entre 0 e 10: '))
while n1 > 10 or n1 < 0:
    print('VALOR INVÁLIDO')
    n1 = int(input('Digite uma nota entre 0 e 10: '))

print(n1)
