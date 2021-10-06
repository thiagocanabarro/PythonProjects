# Desenvolva um programa que pergunte a distância de uma viagem em KM. Calcule o preço da passagem, cobrando R$0,50 por km para viagens de até 200KM
# e R$ 0,45 para viagens mais longas.

kms = int(input("Qual é a distância percorrida na viagem ? "))
mais = (kms * 0.45)
menos =(kms * 0.50)
if kms >= 200:
    print("o preço da sua viagem ficou R$: {}".format(mais))
else:
    print("O preço da sua viagem ficou R$: {}".format(menos))