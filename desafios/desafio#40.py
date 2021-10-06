# Crie um programa que leia duas notas de um aluno e calcule sua média, mostrando uma mensagem no final, de acordo com a média atingida.
# Média abaixo de 5.0 - REPROVADO
# Média entre 5.0 e 6.9 - RECUPERAÇÃO
# Média 7.0 ou superior - APROVADO

cores = {"normal":"\33[m",
         "azul":"\33[34m",
         "amarelo":"\33[33m",
         "vermelho":"\33[41m",
         "roxo":"\33[35m",
         "pretoebranco":"\33[7:30m",
         "verde":"\33[32m",
         "ciano":"\33[36m",
         "cinza":"\33[37m",}


n1 = float(input("Digite a nota que você tirou no primeiro teste: "))
n2 = float(input("Digite a nota que você tirou no segundo teste: "))
n3 = float(input("Digite a nota que você tirou no terceiro teste: "))

me = ((n1+n2+n3) / 3)

if me >= 7:
    print ("Sua média foi de {}{:.2f}{} Você foi aprovado! PARABÉNS!".format(cores["vermelho"],me,cores["normal"]))
elif me >= 5.0 and 6.9:
    print ("Sua média foi de {}{:.2f}{} Que pena, você está de recuperação!".format(cores["vermelho"],me,cores["normal"]))
elif me < 4.9:
    print ("Sua média foi de {}{:.2f}{} Você foi reprovado!".format(cores["vermelho"],me,cores["normal"]))