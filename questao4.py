nota1 = float(input("Primeira nota: "))
nota2 = float(input("Segunda nota: "))
media = (nota1 + nota2)/2
print(f"Tirando {nota1:.1f} e {nota2:.1f}, a média do aluno é {media:.1f}.")



if media>=7.0:
    print('O aluno está \033[34mAPROVADO!\033[0m')
elif 5.0 <= media < 6.9:
    print('O aluno está de \033[33mRECUPERAÇÃO!\033[0m')
else:
    print('O aluno está \033[31mREPROVADO!\033[0m')