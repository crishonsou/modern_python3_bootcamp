num_final = int(input('Calcular o Fatorial de: '))
fatorial = 1

for contador in range(1, num_final + 1):
    fatorial = fatorial * contador
print(f'O fatorial de {num_final} é igual a {fatorial}')
