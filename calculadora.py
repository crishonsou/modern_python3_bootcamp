#### Algoritmo Calculadora

num1 = int(input("Digite o primeiro número: "))
oper = input("Digite a operação: ")
num2 = int(input("Digite o segundo número: "))

resultado = 0

for char in oper:
    if oper == "+":
        resultado = num1 + num2
    if oper == "-":
        resultado = num1 - num2
    if oper == "*":
        resultado = num1 * num2
    if oper == "/":
        resultado = num1 / num2
    else:
        print("Você digitou uma operação inválida!")
        
print(resultado)
        
