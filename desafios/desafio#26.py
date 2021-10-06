#Faça um programa que leia um frase pelo teclado e mostre:
# > quantos vezes aparece a letra "a"
# > em que posição ela aparece a primeira vez
# > em que posição ela aparece a ultima vez

frase = str(input("Digite uma frase: ")).upper().strip()

print ("A primeira letra A aparece {} vezes na frase".format(frase.count("A")))
print ("A letra A aparece pela primeira vez na posição: {} ".format(frase.find("A")+1))
print ("A letra a aparece pela ultia vez na posição: {}".format(frase.rfind("A")+1))