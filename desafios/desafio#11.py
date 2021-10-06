# Faça um programa que leia a largura e a altura de uma parede em metros, calcule a sua área e a quantidade de tinta
# necessária para pintá-la, sabendo que cada litro de tinta pinta uma área de 2m²

a = float(input("Digite a altura da sua parede:"))
l = float(input("Digite a largura da sua parede:"))

area = a * l

litros = area * 0.5

print ("Você poderá pintar esta parede com {} litros de tinta".format(litros))