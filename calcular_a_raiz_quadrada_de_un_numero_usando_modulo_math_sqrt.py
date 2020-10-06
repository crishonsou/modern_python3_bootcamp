def squareRoot(num):
    import math
    answer = math.sqrt(num)
    return answer



num = int(input('Digite um número: '))

resultado = squareRoot(num)

print(f'A raiz quadrad de {num} é {resultado:.0f}')
