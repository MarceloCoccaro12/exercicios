h=float(input("Digite sua altura:"))
sexo=input("Digite seu sexo:")

if (sexo=="Masculino"):
    pesoidealm= (72.7*h)-58
    print("Peso ideal:{:.2f}".format(pesoidealm))

elif (sexo=="Feminino"):
    pesoidealf= (62.1*h)-44.7
    print("Peso ideal:{:.2f}".format(pesoidealf))

else:
    print("\n Reinicie o programa.")