# Faça um programa que leia um ano qualquer e mostre se ele é bissexto

ano = int(input("Em que ano você está? "))

if ano % 4 == 0:
    print ("Você está em ano bissexto")
else:
    print ("Esse não é um ano bissexto")


