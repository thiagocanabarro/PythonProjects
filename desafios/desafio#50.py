#Desenvolva um programa que leia seis números inteiros e mostre a smora apenas daqueles que forem pares. Se o valor digitado for impar. desconsidere-o.

soma = 0
cont = 0

for c in range (1, 7):
    n = int(input("Digite qualquer número inteiro: "))
    if n % 2 == 0:
        soma = soma + n
        cont = cont + 1
print("Você informou {} números PARES e a soma foi {}".format(cont,soma))


