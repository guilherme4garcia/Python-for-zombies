## 1
##
## a = float(input('Digite a medida do lado A: '))
## b = float(input('Digite a medida do lado B: '))
## c = float(input('Digite a medida do lado C: '))
##
## if a < b + c and b < a + c and c < a + b:
##     print('Os valores A, B e C podem formar um triângulo.')
##
##     if a != b != c != a:
##         print('Estes valores formam um triângulo ESCALENO')
##     elif a == b == c:
##         print('Estes valores formam um triângulo EQUILÁTERO')
##     else:
##         print('Estes valores formam um triângulo ISÓSCELES')
##
## else:
##     print('Não é possível formar um triângulo com esses valores.')
##
## 2
##
## ano = int(input('Informe o ano que gostaria de saber se é ou não bissexto: '))
##
## if ano % 4 == 0 and ano % 100 != 0 or ano % 400 == 0:
##     print(f'O ano {ano} é bissexto.')
## else:
##     print(f'O ano {ano} não é bissexto.')
##
## 3
##
## peso = float(input('Digite o peso dos peixes em quilogramas: '))
##
## if peso > 50:
##    excesso = peso - 50
##    multa = excesso * 4
##
## else:
##     excesso = 0
##     multa = 0
##
## print(f'João Papo-de-Pescador excedeu {excesso} kg, o valor da multa será de R${multa:.2f}')
##
## 4
##
## n1 = int(input('Digite o primeiro número: '))
## n2 = int(input('Digite o segundo número: '))
## n3 = int(input('Digite o terceiro número: '))
##
## if n1 > n2 and n1 > n3:
##     print(f'O maior é: {n1}')
##
## if n2 > n1 and n2 > n3:
##     print(f'O maior é: {n2}')
##
## if n3 > n1 and n3 > n1:
##     print(f'O maior é: {n3}')
##
## 5
##
## n1 = int(input('Digite o primeiro número: '))
## n2 = int(input('Digite o segundo número: '))
## n3 = int(input('Digite o terceiro número: '))
## menor = n1
## maior = n1
##
## if n2 < n1 and n2 < n3:
##     menor = n2
##
## if n3 < n1 and n3 < n2:
##     menor = n3
##
## if n2 > n1 and n2 > n3:
##     maior = n2
##
## if n3 > n1 and n3 > n2:
##     maior = n3
##
## print(f'O menor valor digitado foi {menor}')
## print(f'O maior valor digitado foi {maior}')
##
## 6
##
 salario_hora = float(input('Quanto você ganha por hora: '))
 hora_mes = float(input('Quantas horas trabalhadas no mês: '))

 salario_bruto = salario_hora * hora_mes
 imposto_renda = salario_bruto * 0.11
 inss = salario_bruto * 0.08
 sindicato = salario_bruto * 0.05
 descontos = imposto_renda + inss + sindicato
 salario_liquido = salario_bruto - descontos

 print(f'A) + Salário Bruto: R${salario_bruto:.2f}')
 print(f'B) - IR (11%): R${imposto_renda:.2f}')
 print(f'C) - INSS (8%): R${inss:.2f}')
 print(f'D) - Sindicato (5%): R${sindicato:.2f}')
 print(f'E) = Salário Líquido: R${salario_liquido:.2f}')
##
## 7
##
## area = int(input('Qual o tamanho em m² da área a ser pintada: '))
## tinta = area / 3
##
## if area % 54 != 0:
##     latas = int(area / 54) + 1
## else:
##     latas = area / 54
## 
## custo = latas * 80
##
## print(f'Você precisará de {latas} lata(s), irá custar R${custo:.2f}')
