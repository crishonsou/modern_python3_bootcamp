### Algoritmo para multiplicação de dois números positivos

## Início

## Declaração de variáveis

## numero1, numero2, resultado, contador: INTEIRO(int)

numero1 = int(input('Digite o primeiro número: '))
numero2 = int(input('Digite o segundo número: '))
resultado = 0
contador = 0

## Função

while contador < numero2:
    resultado = resultado + numero1
    contador = contador + 1

print('O resultado da multiplicação é: ', resultado)


