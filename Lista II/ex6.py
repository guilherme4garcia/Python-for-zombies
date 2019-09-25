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
