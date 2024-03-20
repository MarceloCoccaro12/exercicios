n1= float(input("Digite sua nota:"))
n2= float(input("Digite sua nota:"))
media= (n1+n2)/2
if (media >= 5):
    print("Aprovado")
else:
    if (media >= 3):
        print("Exame")
    else:
        print("Reprovado")