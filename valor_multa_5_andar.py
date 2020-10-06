## Algoritmo CalculoMulta

## Libs
from datetime import datetime


## Variáveis

data_inicial = datetime.strptime('2020-02-07', '%Y-%m-%d')
print('Data do Inicio do contrato: ', data_inicial)
data_final = datetime.strptime('2020-08-29', '%Y-%m-%d')
print('Data projetada de saida: ', data_final)
dias_corridos = abs((data_final - data_inicial).days)
print('Dias corridos desde a alocação: ', dias_corridos)
aluguel = 3177
va = aluguel * 3
print(f'Valor do aluguel para calculo de multa é de R$ {va:.2f}')
pcm = 366
valor_multa = va * (pcm - dias_corridos) / pcm
print(f'O valor da multa é de R$ {valor_multa:.2f}')


## Custos de mudança

aluguel_plus = 3900
luz = 60
mudança = 2000
pintura = 1000
custo_de_mudança = aluguel_plus + luz + mudança + pintura
print('Custo da mudança: ', custo_de_mudança)

investimento_mudança = valor_multa + custo_de_mudança
print(f'Custo total de mudança é de R$ {investimento_mudança:.2f}')


## Tempo de Recuperação do Investimento

