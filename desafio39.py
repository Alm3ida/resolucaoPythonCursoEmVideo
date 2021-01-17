"""
Faça um programa que leia o ano de nascimento de um jovem e informe, de acordo com sua idade:
- Se ele ainda vai se alistar ao serviço militar.
- Se é a hora de se alistar.
- Se já passou o tempo do alistamento.

Seu programa também deverá mostrar o tempo que falta ou que passou do prazo
"""
age = int(input('Digite a sua idade: '))

if age < 17:
    print('Ainda irá se alistar ao serviço militar, no prazo de {} anos' .format((17-age)))
elif age in range(17, 19):
    print('Está na hora de se alistar!!!')
else:
    print('Já passou do tempo de se alistar!, já se foram {} anos' .format(age-18))