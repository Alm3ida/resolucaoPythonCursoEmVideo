"""
Escreva um programa que faça o computador "pensar" em um número inteiro entre 0 e 5 e peça para o usuário
tentar descobrir qual foi o número escolhido pelo computador. O programa deverá escrever na tela se o usuario
venceu ou perdeu.
"""
from random import randint
from time import sleep


ncomp = randint(0,5) #Faz o sorteio
print('-=-'* 10)
print('Estou pensando em um número entre 0 e 5, advinhe qual:')
print('-=-'* 10)
n = int(input('Digite o número que pense:'))
print('PROCESSANDO...')
sleep(2)
if n == ncomp:
    print('Parabéns, você acertou, eu pensei no número {}' .format(ncomp))
else: 
    print('Você errou, eu pensei no número {}' .format(ncomp))

