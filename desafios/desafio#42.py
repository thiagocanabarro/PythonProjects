# Refaça o exercicio 35. Acrescentando o recurso de mostrar que tipo de triângulo será formado
# Equilatero todos os lados iguais
# Isósceles dois lados iguais
# Escaleno todos os lados diferentes


l1 = float(input("Digite o comprimento do primeiro lado do triângulo: "))
l2 = float(input("Digite o comprimento do segundo lado do triângulo: "))
l3 = float(input("Digite o comprimento do terceiro lado do triângulo: "))

if l1 < l2 + l3 and l2 < l1 + l3 and l3 < l1 + l2:
    print ("Os segmentos acima PODEM FORMAR um triângulo:")
    if l1 == l2 == l3:
        print ("EQUILATERO")
    elif l1 == l2 or l2 == l3 or l1 ==l3:
        print ("ISÓCELES")
    else:
        print ("ESCALENO")

else:
    print ("Os segmentos acima NÃO PODEM FORMAR um triângulo")
