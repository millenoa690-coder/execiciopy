def aprovados(notas):
    lista = []
    for nota in notas:
        if nota >= 7:
            lista.append(nota)
    return lista

notas = [5, 7, 8.5, 6, 10]
print("Notas aprovadas:", aprovados(notas))