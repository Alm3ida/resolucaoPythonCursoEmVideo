""" Refaça o DESAFIO 51, lendo o primeiro termo e a razão de uma PA, mostrando os 10 primeiros termos da
progressão usando a estrutura while.
"""
a1 = int(input('Digite o primeiro termo: '))
razao = int(input('Digite a razão da PA: '))
c = 0
#Uma PA é algo do tipo. (a1, a1 + r, a1 + 2r, a1+ 3r, )
#A quantidade N de termos significa um total de (N-1) somas de 'r' ao a1.
 
print('Calculando os termos da PA')
while c < 10:
    print(f'{a1}, ', end='')
    c += 1
    a1 += razao
