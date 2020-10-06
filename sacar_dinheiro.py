### Algoritmo "SacarDinheiro"

# Variáveis

saldoDisp = 1000
valorSaque = int(input('Digite valor do saque: '))


if valorSaque <= saldoDisp:
    saldoDisp = saldoDisp - valorSaque
    print('Valor do Saque R$ ', valorSaque)
    print('Saldo Disponível: R$ ', saldoDisp)
else:
    print('Valor solicitado é maior que o valor disponível para saque!')
    print('Saldo Disponível: R$ ', saldoDisp)

    
