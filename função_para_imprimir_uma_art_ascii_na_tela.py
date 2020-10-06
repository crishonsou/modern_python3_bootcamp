# Instalar o pacote pyfliget via pip

# pip install pyfiglet==0.8.post1


def printArt(msg, font, color):
    import pyfiglet as pf
    from termcolor import colored

    valid_colors = ('red', 'blue', 'green', 'yellow', 'magenta', 'cyan') 
    valid_fonts = (
        'slant',
        '3-d',
        '3x5',
        '5lineoblique',
        'alphabet',
        'banner3-D',
        'doh',
        'isometric1',
        'alligator',
        'dotmatrix',
        'bubble',
        'bulbhead',
        'digital')

    if font not in valid_fonts:
        font = 'slant'

    if color not in valid_colors:
        color = 'blue'

    art = pf.figlet_format(msg, font=font)
    colored_ascii = colored(art, color=color)
    return colored_ascii


msg = input('Qual a mensagem deseja imprimir?: ')

font = input('Qual fonte?: ')

color = input('Qual cor?: ')

result = printArt(msg, font, color)

print(result)
