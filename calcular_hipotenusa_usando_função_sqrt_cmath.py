import math

num_1 = int(input('Digite o valor do primeiro cateto do triângulo retângulo: '))
num_2 = int(input('Digite o valor do segundo cateto do triângulo retângulo: '))

hipotenusa = math.sqrt(num_1 * num_1 + num_2 * num_2)

print(f'O valor da hipotenusa é: {hipotenusa:.0f} graus')
