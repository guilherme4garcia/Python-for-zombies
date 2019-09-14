s = float(input('Digite o valor do salário: '))
p = float(input('Digite a porcentagem de aumento: '))
x = p / 100 * s
t = s + x
print(f'Com um acréscimo de {p}%, o salário passará de R${s:.2f} para R${t:.2f}. Uma diferença de R${x:.2f}. ')
