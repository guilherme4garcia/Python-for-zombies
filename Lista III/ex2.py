user = str(input('Digite um nome de usuário: '))
senha = str(input('Digite uma senha: '))

while user == senha:
    print('O nome de usuário não pode ser igual a senha.')
    user = str(input('Digite um nome de usuário: '))
    senha = str(input('Digite uma senha: '))

