num = int(input('Digite um número: '))

print(f'Gerando a tabuada do {num}')

for i in range(1, 11):
    resultado = num * i
    print(f'{num} x {i} = {resultado}')
