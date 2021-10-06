#Faça um algoritmo que leia o preço de um produto e mostre seu novo preço, com 5% de desconto

p = int(input("Qual o preço do produto? "))

d = p * 0.95

print ("O preço original deste produto é R$: {} com desconto de 5% você pagará R$: {}".format(p,d))
