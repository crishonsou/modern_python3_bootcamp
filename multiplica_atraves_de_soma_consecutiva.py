num1 = int(input('Digite primeiro numero para multiplicação: '))
num2 = int(input('Digite o segundo numero para multiplicação: '))

i = 0
soma = 0

while i < num2:
    soma = soma + num1
    i = i + 1
print(f'O resultado da multiplicação é: {soma}')

