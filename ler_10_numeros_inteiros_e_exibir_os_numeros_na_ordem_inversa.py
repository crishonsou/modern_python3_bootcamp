vetor_1 = []

for i in range(0, 11 -1):
    i += 1
    vetor_1.append(int(input(f'Digite o número {i} de 10: ')))

print(vetor_1[:: - 1])
