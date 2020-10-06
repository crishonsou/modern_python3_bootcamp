vetor = []


for i in range(0, 21 - 1):
    i += 1
    vetor.append(int(input(f'Digite o valor {i} de 20: ')))

print(vetor)
print('A soma dos numeros digitados é: ', sum(vetor))
