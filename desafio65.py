"""
Crie um programa que leia vários números inteiros pelo teclado. No final da execução, mostre a média entre todos
os valores e qual foi o maior e o menor valores lidos. O programa deve perguntar ao usuário se ele quer ou 
não continuar a digitar valores.

"""
continuar = True
soma = quant = 0
maior = menor = 0

while continuar == True:
    num = int(input('Digite um número inteiro: '))
    if quant == 0:
        maior = menor = num
    if num >= maior:
        maior = num
    elif num < menor:
        menor = num
    quant += 1
    soma += num

    condição = str(input('Deseja continuar? [S/N]')).strip().upper()
    if condição in 'Nn':
        continuar = False
    else:
        continuar = True

if quant == 1:
    menor = maior

print(f'A média aritmética é de {soma/quant:.2f}. O maior valor foi {maior} e o menor valor foi {menor}')

