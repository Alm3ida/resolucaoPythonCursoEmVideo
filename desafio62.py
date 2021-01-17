"""
Melhore o DESAFIO 061, perguntando para o usuário se ele quer mostrar mais alguns termos. O programa encerra
quando ele disser que quer mostrar 0 termos.
"""
a1 = int(input('Digite o primeiro termo: '))
razao = int(input('Digite a razão da PA: '))
c = 0
#Uma PA é algo do tipo. (a1, a1 + r, a1 + 2r, a1+ 3r, )
#A quantidade N de termos significa um total de (N-1) somas de 'r' ao a1. 
print('Calculando os termos da PA')
tot = 0

while c <= 9:
    print(f'{a1}, ', end='')
    c += 1
    a1 += razao
    tot += 1
a1 -= razao
state = True
while state == True:
    quantmais = int(input('Quantos termos você quer mostrar a mais?: '))
    
    for g in range(1, quantmais+1):
        a1 += razao
        print(f'{a1}, ', end='')
        tot += 1
    if quantmais == 0:
        state = False
print(f'Progessão finalizada com {tot} termos')
print('FIM')



