numero = int(input('Digite um número: '))
count = 0
mult = 0

while mult <= numero or count < 2:
    mult += 1
    x = numero % mult
    if x == 0:
        count += 1      
        
if count <= 2:
    print(f'{numero} é um número primo')
else:
    print(f'{numero} não é um numero primo.')
