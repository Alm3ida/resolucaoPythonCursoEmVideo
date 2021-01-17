rel = int(input('Quanto você possui? R$: '))

c = 3.27
dol = (rel/c)

print('Você pode comprar USD{:.2f} com a quantia de {:.2f}' .format(dol, rel))