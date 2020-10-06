elementos = []
pares = []

for i in range(0, 11 - 1):
    i += 1
    elementos.append(int(input(f'Digite o {i} número: ')))
for j in range(len(elementos)):
    if elementos[j] % 2 != 1 and elementos[j] > 0:
        pares.append(elementos[j])
   
print(f'Números digitados foram: {elementos}')
print(f'Estes são os números pares acima de 0: {pares}')

