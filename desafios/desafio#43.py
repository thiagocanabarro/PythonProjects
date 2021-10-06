# Desenvolva uma lógica que leia o peso e a altura de uma pessoa, calcule seu IMC e mostre seu status
# Abaixo de 18.5 - ABAIXO DO PESO
# Entre 18.5 e 25 - PESO IDEAL
# 25 até 30 - SOBREPESO
# 30 até 40 - OBESIDADE
# Acima de 40 - OBESIDADE MÓRBIDA

peso = float(input("Digite seu peso: "))
altura = float(input("Digite sua altura: "))

imc = (peso/altura**2)

print ("Seu índice de massa corporal é {:.2f}".format(imc))

if imc < 18.5:
    print ("Sua categoria é ABAIXO DO PESO")
elif 18.5 <= imc < 25:
    print("Sua categoria é PESO IDEAL")
elif 18.5 <= imc < 30:
    print("Sua categoria é SOBREPESO")
elif 30 <= imc < 40:
    print("Sua categoria é OBESIDADE")
elif imc >= 40:
    print("Sua categoria é OBESIDADE MÓRBIDA")