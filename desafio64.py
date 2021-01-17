"""
Crie um programa que leia varios numeros inteiros pelo teclado. O programa só vai parar quando o usuário
digitar o valor 999, que é a condição de parada. No final, mostre quantos números foram digitados e qual foi
a soma entre eles (desconsiderando o flag)
"""
condição = True
contador = soma = 0

while condição == True:
    inteiro = int(input('Digite um número inteiro [Digite 999 para parar]: '))

    if inteiro != 999:
        soma += inteiro
        contador += 1
    else:
        condição = False
print('Acabou')
print(f'O valor da soma dos {contador} valores é de {soma}')