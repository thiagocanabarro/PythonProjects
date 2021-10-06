# Elabore um programa que calcule o valor a ser pago por um produto considerando seu preço normal e condição de pagamento
# a vista dinheiro/cheque - 10% desconto
# a vista no cartão: 5% desconto
# até 2x no cartão: preço normal
# 3x ou mais no cartão: 20% de juros

valor = float(input("Digite o valor do produto: "))

um = (valor*0.90)
dois = (valor*0.95)
tres = (valor)
quatro = (valor+(valor*0.20))

print ("As opções de pagamento são:")
print ("[ 1 ] a vista dinheiro/cheque: 10% desconto")
print ("[ 2 ] a vista no cartão: 5% desconto")
print ("[ 3 ] até 2x no cartão: preço normal")
print ("[ 4 ] 3x ou mais no cartão: 20% de juros")

opcao = int(input("Digite a opção que deseja pagar :"))

if opcao == 1:
    print ("Você pagará R$: {}".format(um))
elif opcao == 2:
    print ("Você pagará R$: {}".format(dois))
elif opcao == 3:
    print ("Você pagará R$: {}".format(tres))
elif opcao == 4:
    print ("Você pagará R$: {}".format (quatro))
else:
    print ("Opção inválida. Tente novamente.")