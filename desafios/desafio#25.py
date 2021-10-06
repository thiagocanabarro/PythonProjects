# Crie um programa que leia o nome de uma pessoa e diga se ela tem " SILVA " no nome

nome = str(input("Digite seu nome completo: ")).strip()

print ("Seu nome tem silva? {}".format("silva" in nome.lower()))

## Nesse exercicio aprendemos que:
#
# "in" serve para verificar se A é membro de B. Neste caso foi usado para saber se a str 'silva' estava dentro da str 'nome'
# o "strip" retira espaços em branco no começo e no fim
