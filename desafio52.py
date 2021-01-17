"""
Faça um programa que leia um número inteiro e diga se ele é ou não um número primo.
"""
from time import sleep
t = 0
n = int(input('Digite um número: '))

for c in range (1, n+1):
    if (n % c) == 0:
        t += 1
        print('\033[;33m{}\033[m' .format(c), end=' ')
    else:
        print('\033[m{}\033[m' .format(c), end=' ')
sleep(2)

if t < 3:
    print('\nEsse número é primo')
else:
    print('\nEsse número é composto!!!')