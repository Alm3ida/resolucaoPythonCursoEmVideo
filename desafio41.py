"""
A confederação Nacional de Natação precisa de um programa que leia o ano de nascimento de um atleta e mostre
sua categoria, de acordo com a idade:

-Até 9 anos: MIRIM
-Até 14 anos: INFANTIL:
-Até 19 anos: JÚNIOR:
-Até 20 anos: SÊNIOR
-Acima: MASTER
"""
from datetime import date

year = int(input('Digite o ano de seu nascimento: '))
age = date.today().year - year
if age in range(0,10):
    print('Categoria MIRIM')
elif age in range(10,15):
    print('Categoria INFANTIL')
elif age in range(15,20):
    print('Categoria JÚNIOR')
else:
    print('Categoria MASTER')

