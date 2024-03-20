a=int(input("Digite um valor positivo:"))
b=int(input("Digite um valor positivo:"))
c=int(input("Digite um valor positivo:"))

media= (a+b+c)/3

if (a>b) and (a>c):
    maior=a
if (b>a)  and (b>c):
    maior=b
if (c>b) and (c>a):
    maior=c

if (a<b) and (a<c):
    menor=a
if (b<a)  and (b<c):
    menor=b
if (c<b) and (c<a):
    menor=c

print("O menor número digitado foi", menor)
print("O maior número digitado foi", maior)
print("Média:", media)