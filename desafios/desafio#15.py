# Escreva um programa que pergunte a quantidade de KM percorridos por um carro alugado.
# Calcule o preço a pagar, sabendo que o carro custa R$60 por dia e R$0.15 por KM rodado.

km = float(input("Digite a quantidade de quilômetros que você percorreu com o carro: "))
dias = int(input("Digite quantos dias você utilizou o carro:"))

preço = ((dias*60)+(km*0.15))

print ("Você terá de pagar R${}, pela utilização do carro. Você rodou {} quilômetros e utilizou o carro por {} dias".format(preço,km,dias))