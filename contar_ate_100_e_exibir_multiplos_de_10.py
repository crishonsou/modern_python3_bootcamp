numero_inicial = 1
numero_final = int(input('Calcular os múltiplos de 10 até: '))
contador = 1

while contador < numero_final:
    print(contador + 1)
    contador += 1
    if contador % 10 == 0:
        print(f'{contador} é um múltiplo de 10')
