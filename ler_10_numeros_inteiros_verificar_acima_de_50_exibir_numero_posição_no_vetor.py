lista = []
i = 0
numeros = int(input('Digite a quantidade de numeros da lista: '))

while i < numeros:
    i += 1
    numero = int(input(f'Digite o número {i} de {numeros}: '))
    lista.append(numero)
    
print(lista)

for k in range(len(lista)):
    if lista[k] >= 50:
        print(f'A posição do número {lista[k]} no vetor é: {lista.index(lista[k])}')
    



