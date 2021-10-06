# Escreva um programa que leia dois números inteiros e compare-os, mostrando na tela uma mensagem:
# - 0 primeiro valor é maior
# - 0 segundo valor é maior
# Não existe valor maior, os dois são iguais

n1 = int(input("Digite o primeiro número: "))
n2 = int(input("Digite o segundo número: "))

if n1 > n2:
    print("o primeiro número é maior")
elif n2 > n1:
    print ("o segundo número é maior")
elif n1 == n2:
    print (" Não existe valor maior. Os números são iguas")
