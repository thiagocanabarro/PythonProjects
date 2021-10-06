# Escreva um programa que leia a velocidade de um carro
# Se ele ultrapassar 80km/h, mostre uma mensagem dizendo que ele foi multado
# a multa vai custar 7,00 por cada km acima do limite

vel = float(input("Digite a velocidade detectada: "))
multa = (vel - 70) * 7.0

if vel > 70 :
    print("sua velocidade foi de {}, você foi multado em R$ {} reais".format(vel,multa))

else:
    print("Você está dentro da velocidade permitida.")
