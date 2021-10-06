# Escreva um programa que pergunte o salário de um funcionário e calcule o valor do seu aumento
# Para salários superiores a R$1.250.00, Calcule um aumento de 10%
# Para os inferiores ou iguais, o aumento é de 15%

sal = float(input("Digite o salário que você recebe:"))

salplus = (sal + (sal * 0.10))
salmenos = (sal + (sal*0.15))

if sal > 1250:

    print("Você receberá um aumento de 10%, e passará a receber {}".format(salplus))
else:

    print ("Você receberá um aumento de 15% e passará a receber {}".format(salmenos))
