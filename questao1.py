numero = int(input("Digite um número inteiro:"))
while True:
    if numero % 2 == 0:
        print("Par")
        break     
    else:
        print("Ímpar. Tente novamento!")
        numero = int(input("Digite um número inteiro:"))