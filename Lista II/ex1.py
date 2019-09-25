a = float(input('Digite a medida do lado A: '))
b = float(input('Digite a medida do lado B: '))
c = float(input('Digite a medida do lado C: '))

if a < b + c and b < a + c and c < a + b:
    print('Os valores A, B e C podem formar um triângulo.')

    if a != b != c != a:
        print('Estes valores formam um triângulo ESCALENO')
    elif a == b == c:
        print('Estes valores formam um triângulo EQUILÁTERO')
    else:
        print('Estes valores formam um triângulo ISÓSCELES')

else:
    print('Não é possível formar um triângulo com esses valores.')

