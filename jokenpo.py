import random
from time import sleep
cores = {'limpa': '\033[m', 
        'vermelho': '\033[31m',
        'verde': '\033[32m'}

maquina = ['Pedra', 'Papel', 'Tesoura']
jogadaMaquina = random.choice(maquina)
jogador = str(input('Pedra, Papel ou Tesoura? '))

print('JO')
sleep(1)
print('KEN')
sleep(1)
print('PO!!')

if jogadaMaquina == jogador:
    #EMPATE
    print('A máquina escolheu {}, e você {}, portanto EMPATE.'.format(jogadaMaquina, jogador))
elif jogadaMaquina == 'Pedra' and jogador == 'Papel':
    #PEDRA X PAPEL
    print('Você {}VENCEU!!{}'.format(cores['verde'], cores['limpa']))
    print('A máquina escolheu {}, e você {}.'.format(jogadaMaquina, jogador))
elif jogadaMaquina == 'Pedra' and jogador == 'Tesoura':
    #PEDRA X TESOURA
    print('Você {}PERDEU!!{}'.format(cores['vermelho'], cores['limpa']))
    print('A máquina escolheu {}, e você {}.'.format(jogadaMaquina, jogador))
elif jogadaMaquina == 'Papel' and jogador == 'Pedra':
    #PAPEL X PEDRA
    print('Você {}PERDEU!!{}'.format(cores['vermelho'], cores['limpa']))
    print('A máquina escolheu {}, e você {}.'.format(jogadaMaquina, jogador))
elif jogadaMaquina == 'Papel' and jogador == 'Tesoura':
    #PAPEL X TESOURA
    print('Você {}VENCEU!!{}'.format(cores['verde'], cores['limpa']))
    print('A máquina escolheu {}, e você {}.'.format(jogadaMaquina, jogador))
elif jogadaMaquina == 'Tesoura' and jogador == 'Pedra':
    #TESOURA X PEDRA
    print('Você {}VENCEU!!{}'.format(cores['verde'], cores['limpa']))
    print('A máquina escolheu {}, e você {}.'.format(jogadaMaquina, jogador))
elif jogadaMaquina == 'Tesoura' and jogador == 'Papel':
    #TESOURA X PAPEL
    print('Você {}PERDEU!!{}'.format(cores['vermelho'], cores['limpa']))
    print('A máquina escolheu {}, e você {}.'.format(jogadaMaquina, jogador))