n1 = int(input('Primeiro valor: '))
n2 = int(input('Segundo valor: '))
opcao = 0
while opcao!=5:
    print('''    [ 1 ] Somar
    [ 2 ] Multiplicar
    [ 3 ] Maior
    [ 4 ] Novos números
    [ 5 ] Sair do programa''')
    opcao = int(input('>>>>> Qual é a sua opção? '))
    if opcao == 1:
        soma = n1 + n2
        print(f'A soma de {n1} + {n2} é igual a {soma}')
        print('-=-'*12)
    elif opcao == 2:
        multi = n1*n2
        print(f'A multiplicação de {n1} x {n2} é igual a {multi}')
        print('-=-'*12)
    elif opcao == 3:
        if n1>n2:
            print(f'entre {n1} e {n2} o maior é {n1}')
        else:
            print(f'entre {n1} e {n2} o maior é {n2}')
    elif opcao == 4:
        print('Informe os números novamente')
        n1 = int(input('Primeiro valor: '))
        n2 = int(input('Segundo valor: '))
    elif opcao == 5:
        print('Saindo do programa.')
        break
    elif opcao !=1 or 2 or 3 or 4 or 5:
        print('Opção inválida. tente novamente')