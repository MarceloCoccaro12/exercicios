nome=input("Nome do contribuinte:")
cpf=int(input("Digite seu CPF:"))
renda=float(input("Digite sua renda anual:"))
depen=int(input("Digite o número de  dependentes:"))

if (depen >= 1):
    novarenda= renda - depen * (110*12)
    print("Valor:", novarenda)

    if (renda <= 800):
        print("-----------------------------------------------------")
        print("Nome do contribuinte:", nome)
        print("CPF:", cpf)
        print("Valor a ser pago:{:.2f}".format(novarenda))

    elif (renda >= 801) and (renda <= 4000):
        novarenda1= novarenda*1.025
        print("-----------------------------------------------------")
        print("Nome do contribuinte:", nome)
        print("CPF:", cpf)
        print("Valor a ser pago:{:.2f}".format(novarenda1))

    elif (renda >= 4001) and (renda <= 9000):
        novarenda2= novarenda*1.05
        print("-----------------------------------------------------")
        print("Nome do contribuinte:", nome)
        print("CPF:", cpf)
        print("Valor a ser pago:{:.2f}".format(novarenda2))

    elif (renda > 9000):
        novarenda3= novarenda*1.10
        print("-----------------------------------------------------")
        print("Nome do contribuinte:", nome)
        print("CPF:", cpf)
        print("Valor a ser pago:{:.2f}".format(novarenda3))

    else:
        print("Reinicie o programa.")

