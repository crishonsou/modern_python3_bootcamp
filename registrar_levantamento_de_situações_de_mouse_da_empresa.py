qtde_mouse = int(input('Digite a quantidade de mouses: '))
i = 1
esfera = 0
limpeza = 0
cabo_conector = 0
quebrado = 0

print('Códigos de defeito: 1- Esfera 2- Limpeza 3- Cabo/Conector 4- Quebrados/Inutilizados 0- Encerrar Levantamento')


for i in range(qtde_mouse):
    i += 1
    cod_defeito = int(input(f'Digite o código do defeito para o mouse  código {i}: '))
    if cod_defeito >= 5:
        print('Você digitou um código errado.')
        cod_defeito = int(input(f'Digite o código do defeito para o mouse  código {i}: '))
    if cod_defeito == 0:
        print('Você optou por encerrar o levantamento.')
        break
    if cod_defeito == 1:
        esfera += 1
    if cod_defeito == 2:
        limpeza += 1
    if cod_defeito == 3:
        cabo_conector += 1
    if cod_defeito == 4:
        quebrado += 1
    
        
    
total_esfera = esfera
percentual_esfera = total_esfera / qtde_mouse * 100
total_limpeza = limpeza
percentual_limpeza = total_limpeza / qtde_mouse * 100
total_cabo_conector = cabo_conector
percentual_cabo_conector = total_cabo_conector / qtde_mouse * 100
total_quebrado = quebrado
percentual_quebrado = total_quebrado / qtde_mouse * 100
  



print('Quantidade de mouses:', qtde_mouse)

print('Necessita de Esfera: ', total_esfera)
print(f'Percentual (Esfera): {percentual_esfera:.0f} %')

print('Necessita de Limpeza: ', total_limpeza)
print(f'Percentual (Limpeza): {percentual_limpeza:.0f} %')

print('Necessita de Cabo/Conector: ', total_cabo_conector)
print(f'Percentual (Cabo/Conector): {percentual_cabo_conector:.0f} %')

print('Quebrado/Inutilizado ', total_quebrado)
print(f'Percentual (Cabo/Conector): {percentual_quebrado:.0f} %')

        
    
        
    

        


       



        

    
        
    
 









