def media(notas):
    return sum(notas) / len(notas)

notas = []
quantidade = int(input("Quantas notas? "))

for i in range(quantidade):
    nota = float(input("Digite a nota: "))
    notas.append(nota)

print("Média:", media(notas))