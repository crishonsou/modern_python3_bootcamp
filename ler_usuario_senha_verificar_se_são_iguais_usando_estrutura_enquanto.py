nome = input('Digite seu nome: ')
senha = input('Digite uma senha: ')

for letra in range(len(senha)):
    if senha[letra] == nome[letra]:
        print('Você digitou uma senha errada.')
        senha = input('Digite uma senha: ')
    else:
        print('Você digitou a senha corretamente.')
        break
print('Obrigado.')
    
