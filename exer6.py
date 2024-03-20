peso=float(input("Digite o peso dos peixes em quilos:"))

if (peso > 50):
    E=peso-50
    M=E*4
    print("Excesso:", E,"Kg")
    print("Multa:", M, "reais")

else:
    print("Excesso: ZERO")
    print("Multa: ZERO")