sal_atual = int(input('Digite o salário atual: '))


sal_anual = sal_atual * 13
sal_ir = sal_anual * 0.275
sal_anual_liq = sal_anual - sal_ir
plr = sal_atual * 3
plr_ir = plr * 0.275
plr_anual_liq = plr - plr_ir
plano_saude = 700 * 12
previdencia = (sal_atual * 0.10) * 12
alimentacao = 875 * 12
remuneracao_anual = sal_anual + plr + plano_saude + previdencia + alimentacao
remuneracao_anual_ir = remuneracao_anual * 0.275
remuneracao_anual_liq = remuneracao_anual - remuneracao_anual_ir
remuneracao_mensal_pj = remuneracao_anual_liq / 12





print(f'Salário Anual: R$ {sal_anual:.2f}')
print(f'IR anual: R$ {sal_ir:.2f}')
print(f'Salário Anual Liquido: R$ {sal_anual_liq:.2f}')
print(f'Valor do PLR: R$ {plr:.2f}')
print(f'IR sobre PLR: R$ {plr_ir:.2f}')
print(f'PLR Liquido: R$ {plr_anual_liq:.2f}')
print(f'Plano de Saude Anual: R$ {plano_saude:.2f}')
print(f'Previdência Privada Anual: R$ {previdencia:.2f}')
print(f'Alimentação Anual: R$ {alimentacao:.2f}')
print(f'Remuneracao Anual Total: R$ {remuneracao_anual:.2f}')
print(f'IR sobre RAT Anual Total: R$ {remuneracao_anual_ir:.2f}')
print(f'Remuneracao Anual Total Liquida: R$ {remuneracao_anual_liq:.2f}')
print(f'Remuneracao Mensal PJ: R$ {remuneracao_mensal_pj:.2f}')







                
