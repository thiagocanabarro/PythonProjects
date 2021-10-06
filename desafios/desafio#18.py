# Faça um programa que leia um ângulo qualquer e mostre na tela o valor do seno, cosseno e tangente desse ângulo.
from math import radians,sin,cos,tan

ang = float(input("Digite um ângulo:"))

sen = sin(radians(ang))
cos = cos(radians(ang))
tg  = tan(radians(ang))

print ("O angulo de {} tem o SENO de {:.2f}".format(ang, sen))
print ("O angulo de {} tem o COS de {:.2f}".format(ang, cos))
print ("O angulo de {} tem a TAN de {:.2f}".format(ang, tg))