cond=input("Digite o operador que deseja efutar a conta(somar, multiplicar, subtrair e dividir):")
n1=float(input("Digite um número:"))
n2=float(input("Digite outro número:"))

if (cond=="somar"):
    soma=n1+n2
    print(soma)

elif (cond=="multiplicar"):
    mult=n1*n2
    print(mult)

elif (cond=="subtrair"):
    sub=n1-n2
    print(sub)

elif (cond=="dividir"):
    div=n1/n2
    print(div)

else:
    print("Reiniciar o programa.")
    