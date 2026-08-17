n = int(input("Quantos números você vai digitar? "))

contador = 0
soma = 0

while contador < n:
    numero = int(input("Digite um número entre 0 e 1000: "))

    while numero < 0 or numero > 1000:
        print("Número inválido!")
        numero = int(input("Digite novamente: "))

    if contador == 0:
        menor = numero
        maior = numero
    else:
        if numero < menor:
            menor = numero

        if numero > maior:
            maior = numero

    soma += numero
    contador += 1

print("Menor:", menor)
print("Maior:", maior)
print("Soma:", soma)