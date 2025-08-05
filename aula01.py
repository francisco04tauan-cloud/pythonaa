#nome = "lucas"
#idade = 26
#altura = 1.80

#print ("meu nome e", nome , "tenho", idade , "anos e minha altura e", altura , "metros")

#numero1 = 10
#numero2 = 10
#media = (numero1 + numero2) / 2
#print("a media de", numero1, "e", numero2, "é", media, ".")


nome = input("digite seu nome:")
idade = input("digite sua idade:")
altura = input("digite sua altura:")

print("seu nome e", nome)
print("sua idade e", idade)
print("sua altura e", altura)


print("o tipo de dado do nome e", type(nome))
print("o tipo de dado da idade e", type(idade))
print("o tipo de dado da altura e", type(altura))


idade = int(idade)
altura = float(altura)


print("sua idade convertida e", idade)
print("sua altura convertida e", altura)


print("o tipo de dado da idade apos conversao e", type(idade))
print("o tipo de dado da altura apos conversao e", type(altura))