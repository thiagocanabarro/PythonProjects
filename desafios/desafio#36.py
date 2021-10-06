# Escreva um programa para aprovar o empréstimo bancário para a compra de uma casa. O Programa vai perguntar o valor da casa, o salário e em quantos anos
# deseja pagar. Calcule o valor da prestação mensal. Sabendo que ela não pode exceder 30% do salário ou então o empréstimo será negado.

valor = float(input("Digite o valor da casa: "))
salario = float(input("Digite quanto você recebe por mês:"))
anos = int(input("Em quantos anos você deseja pagar a casa? "))

prestacao = (anos * 12)
qtdparcelas = (valor / prestacao)
limite = (salario * 0.30)
parcelamento = (prestacao * limite)

if valor < parcelamento:
    print ("Você poderá comprar esta casa")
else:
    print ("Você não tem dinheiro o suficiente para comprar essa casa, you better work bitch")