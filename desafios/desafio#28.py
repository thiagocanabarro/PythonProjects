# Escreva um programa que faça o computador "pensar" em um número inteiro entre 0 e 5.
# e peça para o usuário tentar descobrir qual foi o número escolhido pelo PC
# o programa deverá escrever na tela se o usuário venceu ou perdeu

from random import choice

lista = [0,1,2,3,4,5]
escolhido = choice(lista)

num = int(input("Pensei em um número de 0 a 5, qual número estou pensando? "))

if escolhido == num:
    print("Você acertou, pensei neste número")
else:
    print("errou")




