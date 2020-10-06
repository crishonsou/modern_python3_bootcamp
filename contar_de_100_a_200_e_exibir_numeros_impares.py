num_1 = int(input('Digite um valor: '))
num_2 = int(input('Digite outro valor: '))
contador = num_1

print(f'Exibindo números impares entre {contador} e {num_2}')

while contador < num_2:
    contador += 1
    if contador % 2 != 0:
        print(contador)
    
