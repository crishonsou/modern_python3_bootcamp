num_final = int(input('Calcular o Fatorial de: '))
fatorial = 1
contador = 1

while contador <= num_final:
    fatorial = fatorial * contador
    contador = contador + 1
print(f'O fatorial de {num_final} é igual a {fatorial}')
