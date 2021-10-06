# Desenvolva um programa que leia o comprimento de três retas e diga ao usuário se elas podem ou não formar um triângulo

l1 = int(input("Digite o comprimento do primeiro lado do triângulo: "))
l2 = int(input("Digite o comprimento do segundo lado do triângulo: "))
l3 = int(input("Digite o comprimento do terceiro lado do triângulo: "))

if l1 < l2 + l3 and l2 < l1 + l3 and l3 < l1 + l2:
    print ("Os segmentos acima PODEM FORMAR um triângulo")
else:
    print ("Os segmentos acima NÃO PODEM FORMAR um triângulo")
