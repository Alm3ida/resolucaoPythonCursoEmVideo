"""
Refaça o Desafio09, mostrando a tabuada de um número que o usuário escolher, só que agora utilizando um laço
for.
"""
n = int(input('Digite o número desejado: '))
print('-.' * 20)
print("A tabuada para o número {} é: " .format(n))
for c in range (0, 11):
    print('{}*{} = {}' .format(n, c, n*c))
print('FIM!!!')
print('-.' * 20)