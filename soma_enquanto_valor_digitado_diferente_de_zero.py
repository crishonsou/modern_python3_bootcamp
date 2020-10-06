##### Algoritmo SomaEnquantoValorDiferenteDe0

## Variáveis

num = int(input('Digite valor para a soma: '))
soma = 0

while num != 0:
    soma += num
    print('Total: ', soma)
    num = int(input(' Digite valor para a soma: '))
print('Resultado: ', soma)
