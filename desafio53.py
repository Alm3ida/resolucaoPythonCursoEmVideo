"""
Crie um programa que leia uma frase qualquer e diga se ela é um palíndromo, desconsiderando os espaços.
Ex:
APOS A SOPA
"""
frase = str(input('Digite a frase a ser analisada: ')).strip().upper()
palavras = frase.split()
juntas = ''.join(palavras)
t = 0
tam = len(juntas)
for c in range (0, tam):
    if juntas[c] == juntas[(tam-1)-c]:
        t += 1


print('Você digitou a frase {}' .format(juntas))
if t == tam:
    print('Essa frase é um Palíndromo!!!')
else:
    print('Que pena, essa frase não é um Palíndromo')

print('A quantidade de duplas corretas é {}'.format(t))
print('O comprimento da frase é {}' .format(tam))

