num_inicial = int(input('Digite um numero: '))
num_final = int(input('Digite outro numero: '))
soma = 0
contador = 0

while contador <= num_final:
    soma = soma + contador
    contador = contador + 1
print(f'A soma entre {num_inicial} e {num_final} é igual a {soma}')
