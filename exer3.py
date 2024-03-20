idade=int(input("Digte sua idade:"))

if (idade < 16):
    print("Não-eleitor")
if (idade >= 18) and (idade <= 65): #Sempre quando for colocar uma condição, colocar entre em parenteses (idade >= 18) and (idade <= 65)
    print("Eleitor obrigatório")
if  (idade >=16) and (idade < 18):
    print("Eleitor facultativo")
if (idade > 65) :
    print("Eleitor facultativo")