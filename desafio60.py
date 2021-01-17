num = int(input('Digite o número desejado: '))

# O Fatorial é definido pela operação !. n! = n(n-1)(n-2)(n-3) ... 2 x 1
c = num
f = 1
print('Calculando o Fatorial de {} ...' .format(num))
while c > 0:
    print(f'{c}', end='')
    print(' x ' if c > 1 else ' = ', end='')
    f *= c
    c -= 1
print(f'{f}')