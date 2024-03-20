peso=float(input("Digite seu peso:"))
h=float(input("Digite sua altura:"))

massa= peso/(h)**2

if (massa < 26):
    print("Normal")

if (massa >= 26) and (massa < 30):
    print("Obeso")

if (massa >= 30):
    print("Obeso Mórbido")