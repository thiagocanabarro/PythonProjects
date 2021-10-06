# Crie um programa que leia o nome completo de uma pessoa e mostre:
# O nome com todas as letras maisculas
# Quantas letras ao todo ( sem considerar os espaços )
# Quantas letras tem o primeiro nome

nome = str(input('Digite seu nome:')).strip()
print ("Seu nome com todas as letras maisculas é {}:".format(nome.upper()))
print ("Seu nome com todas as letras minusculas é {}:".format(nome.lower()))
print ("A quantidade de letras que seu nome tem é {}".format(len(nome)))
print ("A quantidade de letras do seu primeiro nome é {}".format(nome.find(" ")))