## Algoritimo para calculo da média de notas de um aluno

## Inicio

## Declaração de Variáveis

nota1 = int(input('Digite a primeira nota: '))
nota2 = int(input('Digite a segunda nota: '))
nota3 = int(input('Digite a terceira nota: '))
nota4 = int(input('Digite a quarta nota: '))

soma_das_notas = nota1 + nota2 + nota3 + nota4
media_das_notas = soma_das_notas / 4

print('A média das notas é: ', media_das_notas)

if media_das_notas >= 7:
    print("APROVADO")
else:
    print("REPROVADO")

    

    


