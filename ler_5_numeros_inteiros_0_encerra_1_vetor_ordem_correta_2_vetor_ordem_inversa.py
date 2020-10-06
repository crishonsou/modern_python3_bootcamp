vetor = []
i = 0

código = int(input('Digite um código: '))

if código > 0:
    while i < 5:
        i += 1
        valor = int(input('Digite um valor: '))
        vetor.append(valor)
    if código == 1:
        print(vetor[0::])
    if código == 2:
        print(vetor[::-1])
   

       
