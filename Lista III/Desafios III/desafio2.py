# Indique como um troco deve ser dado utilizando-se um número mínimo de notas. Seu
# # algoritmo deve ler o valor da conta a ser paga e o valor do pagamento efetuado desprezando
# # os centavos. Suponha que as notas para troco sejam as de 50, 20, 10, 5, 2 e 1 reais, e que
# # nenhuma delas esteja em falta no caixa

conta = int(input('Digite o valor da conta a ser paga: '))
pagamento = int(input('Digite o valor do pagamento efetuado: '))
troco = pagamento - conta
notas = [50, 20, 10, 5, 2, 1]
total_notas = 0

for x in notas:
    while troco >= x:
        print(f'Uma nota de {x}')
        troco -= x

