nomes = [4]
notas = [3]
media = []
cont_nomes = 1
cont_notas = 1

for i in range(0, 5):
    cont_nomes += 1
    nomes.append(input(f'Digite o nome do aluno(a): '))
    nomes[cont_nomes - 1]
    for j in range(0, 4):
        j += 1
        notas.append(int(input(f'Digite a nota {j} do aluno(a) {nomes[cont_nomes -1]}: ')))
        

for k in range(len(notas)):
    media.append(sum(notas[k : k + 4]) / 4)

for l in range(len(nomes)):
    if media[l] >= 7:
        print(f'O Aluno(a) {nomes[l]} foi aprovado com media {media[l]}')
    else:
        print(f'O Aluno(a) {nomes[l]} foi reprovado com media {media[l]}')
    
    
 



