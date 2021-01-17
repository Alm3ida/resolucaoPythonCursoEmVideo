a = int(input('Primeiro valor: '))
b = int(input('Segundo valor: '))
c = False

while c == False:
    op = int(input('''
    [ 1 ] somar
    [ 2 ] multiplicar
    [ 3 ] maior
    [ 4 ] novos números
    [ 5 ] sair do programa
    >>>>> Qual é a sua opção?: '''))
    if op == 1:
        print(f'A soma {a} + {b} é {a+b} ')
    elif op == 2:
        print(f'O produto {a} * {b} é igual à {a*b}')
    elif op == 3:
        if a > b:
            print(f'O número {a} é o maior')
        elif a == b:
            print(f'O numéro {a} é igual à {b}')
        else:
            print(f'O número {b} é o maior')
    elif op == 4:
        a = int(input('Digite o primeiro valor: '))
        b = int(input('Digite o segundo valor: '))
    elif op == 5:
        print('Finalizando o programa...')
        c = True
    else:
        op = int(input('Opção inválida. Tente novamente...: '))