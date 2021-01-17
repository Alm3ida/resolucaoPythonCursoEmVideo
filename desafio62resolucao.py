print('Gerador de PA')
print('-=' *10)
primeiro = int(input('Primeiro termo: '))
razão = int(input('Razão da PA: '))
termo = primeiro
cont = 1
total = 0
mais = 10
while mais != 0:
    total += mais
    while cont <= total:
        print(f'{termo} -> ', end='')
        termo += razão
        cont += 1
    print('PAUSA')
    mais = int(input('Quantos termos a mais você quer digitar? '))
print(f'Progressão finalizada com {cont} termos mostrados. ')