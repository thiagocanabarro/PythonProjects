#Escreva um programa que leia um número inteiro qualquer e peça para o usuário escolher qual será a base de conversão:
# 1 para binário
# 2 para octal
# 3 para hexadecimal

num = int(input("Digite um número inteiro: "))
print ('''Escolha 1 opção para fazer a conversão desse número:
       "[ 1 ] para converter para binário"
       "[ 2 ] para converter para octal"
       "[ 3 ] para converter para hexadecimal"''')
opcao = int(input("Digite sua opção: "))

if opcao == 1:
    print("O número {} convertido para número BINÁRIO é {}".format(num, bin(num)))
elif opcao == 2:
    print("O número {} convertido para número OCTAL é {}".format(num, oct(num)))
elif opcao == 3:
    print ("O número {} convertido para número HEXADECIMAL é {}".format(num, hex(num)))
else:
    print ("Opção Inválida. Tente novamente.")



