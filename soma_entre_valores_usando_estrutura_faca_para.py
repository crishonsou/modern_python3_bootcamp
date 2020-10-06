num_inicial = int(input('Digite um numero: '))
num_final = int(input('Digite outro numero: '))
soma = 0

for contador in range(num_inicial, num_final + 1):
    soma = soma + contador
print(f'A soma entre {num_inicial} e {num_final} é igual a {soma}')
