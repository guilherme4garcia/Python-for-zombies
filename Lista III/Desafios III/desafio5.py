#Faça um programa que peça um inteiro positivo e o mostre invertido. Ex.: 1234 gera 4321

n = int(input('Digite um número inteiro positivo: '))
inverter = int(str(n)[::-1])
print(inverter)
