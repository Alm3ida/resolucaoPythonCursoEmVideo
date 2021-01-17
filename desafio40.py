"""
Crie um programa que leia duas notas de um aluno e calcule sua média, mostrando uma mensagem no final, de
acordo com a média atingida:
- Média abaixo de 5.0: Reprovado
- Média entre 5.0 e 6.9: Recuperação
- Média 7.0 ou superior: Aprovado 
"""
n1 = float(input('Digite o valor da nota 1: '))
n2 = float(input('Digite o valor da nota 2: '))

average = (n1 + n2) / 2

if average < 5:
    print('Você foi reprovado com média inferior à \033[30;;31m5.0\033[m')
elif average > 5 and average < 7:
    print('Você ficou de recuperação por não atingir nota \033[30;;33m7.0\033[m')
else:
    print('Você foi aprovado por atingir nota igual ou superior a \33[30;;32m7.0\033[m, Parabéns!')

