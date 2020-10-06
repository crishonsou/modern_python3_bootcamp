import string


def alphabetPosition(str1):
    alphabet = list(string.ascii_lowercase)
    posicao = alphabet.index(str1) + 1
    return posicao
    
    



letra = input('Digite letra: ')
posicao = alphabetPosition(letra)
print(f'A letra {letra} está na posição {posicao} do alfabeto')



    
        
        




