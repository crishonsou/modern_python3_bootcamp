vetor_1 = []
vetor_2 = []
vetor_3 = []


for i in range(0, 11 - 1):
    i += 1
    vetor_1.append(int(input(f'Digite o número {i} para o vetor 1: ')))
    
for j in range(0, 11 - 1):
    j += 1
    vetor_2.append(int(input(f'Digite o número {j} para o vetor 2: ')))

for elemA, elemB in zip(vetor_1, vetor_2):
    vetor_3.append(elemA + elemB)
 
  
print(vetor_1)
print(vetor_2)
print(vetor_3)
