"""
Melhore o jogo do DESAFIO 028 onde o computador vai "pensar" em um número entre 0 e 10. Só que agora o jogador
vai tentar adivinhar até acertar, mostrando no final quantos palpites foram necessários para vencer
"""
from random import randint
contagem = 0
numC = randint(0, 10)
numP = int(input('''
Estou pensando em um número entre 0 e 10...
Tente adivinhar qual!: '''))

while numP != numC:
    if numP < numC:
        print('Mais... Tente mais uma vez. ')
        contagem += 1
    else:
        print('Menos... Tente mais uma vez. ')
        contagem += 1
    numP = int(input('Digite novamente: '))
contagem += 1

print(f'Acertou com {contagem} tentativas, Parabéns!!!')