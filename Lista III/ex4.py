n = int(input("Digite um número inteiro para saber seu correspondente na seqüencia de Fibonacci: "))
a = 1
b = 1
count = 1
while n <= 0:
    print('Não é possível utilizar um valor negativo.')
    n = int(input('Digite um número inteiro para saber seu correspondente na sequüencia de Fibonacci: '))

while count <= (n - 1):
    a, b = b, a + b
    count += 1

print(a)