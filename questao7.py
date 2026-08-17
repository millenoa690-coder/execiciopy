contador=0
p1= input("Telefonou para vítima?").upper()
p2 = input ("Esteve no local do crime?").upper()
p3 = input("Mora perto da vítima?").upper()
p4 = input("Devia para a vítima?").upper()
p5 = input("Já trabalhou coma a vítima?").upper()


if p1 in ["SIM",'S']:
    contador+=1
if p2 in ["SIM",'S']:
    contador+=1
if p3 in ["SIM",'S']:
    contador+=1
if p4 in ["SIM",'S']:
    contador+=1
if p5 in ["SIM",'S']:
    contador+=1

if contador == 2:
    print("suspeita")
elif contador == 3 or contador == 4:
    print("cúmplice")
elif contador == 5:
    print("assassino")
else:
    print("inocente")
