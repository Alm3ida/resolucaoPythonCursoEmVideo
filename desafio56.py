"""
Desenvolva um programa que leia o nome, idade e sexo de 4 pessoas. No final do programa, mostre:
> A média de idade do grupo.
> Qual é o nome do homem mais velho.
> Quantas mulheres têm menos de 20 anos.
"""
somaidade = 0
mediaidade = 0
maioridadehomem = 0
nomevelho = ''
quantidademulher = 0
for c in range (1,5):
    print('----- {}º PESSOA -----' .format(c))
    nome = str(input('NOME: ')).strip()
    idade = int(input('Idade: '))
    sexo = str(input('Sexo [M/F]: ')).strip().upper()
    somaidade += idade
    if c == 1 and sexo in 'M':
        maioridadehomem = idade
    if sexo in 'M' and idade > maioridadehomem:
        maioridadehomem = idade
        nomevelho = nome
    if sexo in 'F' and idade < 20:
        quantidademulher += 1
mediaidade = somaidade/4

print('A média da idade do grupo é de {} anos.' .format(mediaidade))
print('O homem mais velho se chama {} e tem {} anos. ' .format(nomevelho, maioridadehomem))
print('A quantidade de mulheres com menos de 20 anos é {}.' .format(quantidademulher))