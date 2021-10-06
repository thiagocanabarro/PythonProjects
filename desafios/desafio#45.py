# Crie um programa que faça o computador jogar Jokenpô com você
from random import randint

itens = ('pedra','papel','tesoura')

computador = randint(0,2)

print ('''Suas opções
[ 0 ] PEDRA
[ 1 ] PAPEL
[ 2 ] TESOURA''')
jogador = int(input("Qual é a sua jogada? "))
print("-="*10)
print('Computador jogou {}'.format(itens[computador]))
print("-="*10)
if computador == 0:#jogou pedra
      if jogador == 0:#jogou pedra
            print("EMPATE!")
      elif jogador == 1:#jogou papel
            print ("PAPEL ENROLA PEDRA. JOGADOR VENCE")
      elif jogador == 2:#jogou tesoura
            print ("PEDRA QUEBRA TESOURA. COMPUTADOR VENCE")
      else:
            print('jogada inválida!')
elif computador == 1:#jogou papel
      if jogador == 0:#jogou pedra
            print("PAPEL ENROLA PEDRA. COMPUTADOR VENCE")
      elif jogador == 1:
            print("EMPATE!")
      elif jogador == 2:#jogou tesoura
            print("PEDRA QUEBRA TESOURA. COMPUTADOR VENCE")
      else:
            print('jogada inválida!')
elif computador == 2:#jogou tesoura
      if jogador == 0:#jogou pedra
            print("PEDRA QUEBRA TESOURA. COMPUTADOR VENCE")
      elif jogador == 1:#jogou papel
            print("TESOURA CORTA PAPEL. COMPUTADOR VENCE")
      elif jogador == 2:#jogou tesoura
            print("EMPATE!")
      else:
            print('jogada inválida!')




