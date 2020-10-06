numero = int(input('Verificar numeros primos até: '))
multiplo = 0

for contador in range(2,numero):
    if (numero % contador == 0):
        print('Multiplo de', contador)
        multiplo += 1
if (multiplo == 0):
    print(f'{numero} é um número primo')
else:
    print(f'{numero} não é um numero primo. Tem {multiplo} multiplo(s) acima de 2 e abaixo de {numero}')
