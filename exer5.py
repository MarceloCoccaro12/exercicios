nome= input("Nome:")
tipoapt= input("Tipo do apartamento(digite em maiúsculo):")
ndiariautil=int(input("Número de diárias ultilizadas:"))
valorconsumo= float(input("Valor de consumo:"))

A=150
B=100
C=75
D=50



if (tipoapt=="A"):
    totaldia=ndiariautil*A
    subtotal= totaldia+valorconsumo
    taxa=subtotal*0.10
    totalgeral= subtotal+taxa
    print("Nome:", nome)
    print("Total da diária: ",totaldia)
    print("Subtotal: ",subtotal)
    print("Total geral: ",totalgeral)

elif (tipoapt=="B"):
    totaldia=ndiariautil*B
    subtotal= totaldia+valorconsumo
    taxa=subtotal*0.10
    totalgeral= subtotal+taxa
    print("Nome:", nome)
    print("Total da diária: ",totaldia)
    print("Subtotal: ",subtotal)
    print("Total geral: ",totalgeral)

elif (tipoapt=="C"):
    totaldia=ndiariautil*C
    subtotal= totaldia+valorconsumo
    taxa=subtotal*0.10
    totalgeral= subtotal+taxa
    print("Nome:", nome)
    print("Total da diária: ",totaldia)
    print("Subtotal: ",subtotal)
    print("Total geral: ",totalgeral)

elif (tipoapt=="D"):
    totaldia=ndiariautil*D
    subtotal= totaldia+valorconsumo
    taxa=subtotal*0.10
    totalgeral= subtotal+taxa
    print("Nome:", nome)
    print("Total da diária: ",totaldia)
    print("Subtotal: ",subtotal)
    print("Total geral: ",totalgeral)

else:
    print("Reinicie o programa.")    