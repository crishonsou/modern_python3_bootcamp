def calculaFatorial(numero):
    fatorial = 1
    contador = 1
    while contador <= numero:
        fatorial = fatorial * contador
        contador += 1       
    return fatorial 





num = int(input('Digite um numero: '))
resultado = calculaFatorial(num)
print(f'O fatorial de {num} é {resultado}')
