"""
Faça um programa que calcule a soma entre todos os números ímpares que são múltiplos de três e que se encontram
no intervalo de 1 a 500.
"""
a = int(input('Digite o começo do intervalo: '))
b = int(input('Digte o fim do intervalo: '))

s = 0
for c in range (a, b + 1):
    if ((c % 3) == 0) and (c % 2) == 1:   
        s += c
print('A soma desses números é igual à {}' .format(s))