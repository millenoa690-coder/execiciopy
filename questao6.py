erros = 0
while erros < 4:

    turno = input("Em que turno você estuda: digite M - matutino V - vespertino ou N - noturno \nresposta:"). upper()

    if turno == 'N':
        print("Noturno")
        break
    elif turno == 'M':
        print("Matutino")
        break
    elif turno == 'V':
        print("Vespertino")
        break
    else:
        erros +=1
        tentaivas_restantes = 4 - erros
        if tentaivas_restantes > 0:
            print(f"Respota inválida! Você ainda tem {tentaivas_restantes} tentativas(s).\n")

if erros == 4:
    print("Limites de 4 tenativas. Programa fechado")