# Crie um algoritmo que leia um número e mostre o seu dobro, triplo e raiz quadrada

n = int(input("Digite um número"))

d = n*2
t = n*3
q = n**(1/2)

print ("o valor dobrado de {} é: {}".format(n,d))
print ("o valor triplo de {} é: {}".format(n,t))
print ("a raiz quadrado de {} é: {}".format (n,q))