"""
Crie um programa que mostre na tela todos os números pares que estão no intervalo entre 1 e 50.
"""
a = int(input('Digite o começo do intervalo: '))
b = int(input('Digite o fim do intervalo: '))

if (a % 2) == 1:
    for c in range (a + 1, b + 1, 2):
        print(c)
else:
    for c in range (a, b + 1, 2):
        print(c)
