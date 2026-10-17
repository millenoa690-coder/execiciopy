def dividir():
    try:
        n1 = float(input("Digite o primeiro número: "))
        n2 = float(input("Digite o segundo número: "))
        resultado = n1 / n2
    except ValueError:
        print("Entrada inválida! Digite apenas números.")
    except ZeroDivisionError:
        print("Não é possível dividir por zero!")
    else:
        print("Resultado:", resultado)

dividir()