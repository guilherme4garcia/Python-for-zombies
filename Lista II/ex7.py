## Faça um programa para uma loja de tintas. O programa deverá pedir o tamanho em metros quadrados da área a
## ser pintada. Considere que a cobertura da tinta é de 1 litro para cada 3 metros quadrados e que a tinta é vendida
## em latas de 18 litros, que custam R$ 80,00. Informe ao usuário a quantidades de latas de tinta a serem
## compradas e o preço total. Obs. : somente são vendidos um número inteiro de latas.


area = int(input('Qual o tamanho em m² da área a ser pintada: '))
tinta = area / 3

if area % 54 != 0:
    latas = int(area / 54) + 1
else:
    latas = area / 54

custo = latas * 80

print(f'Você precisará de {latas} lata(s), irá custar R${custo:.2f}')

