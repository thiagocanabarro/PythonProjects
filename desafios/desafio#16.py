#Crie um programa que leia um númeor Real qualquer pelo teclado e mostre na tela a sua porção inteira
# ex: Digite um número: 6.127. o número 6.127 tem a parte Inteira 6

import math

num = float(input("Digite um valor:"))

print("O valor digitado foi {} e a sua porção inteira é {}".format(num, math.trunc(num)))