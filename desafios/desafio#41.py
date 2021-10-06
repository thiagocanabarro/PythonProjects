#A configuração nacional de natação precisa de um programa que leia o ano de nascimento de um atleta e mostre sua categoria,
# de acordo com sua idade
# Até 9 anos de idade: MIRIM
# Até 14 anos de idade: INFANTIL
# Até 19 anos de idade: JUNIOR
# Até 25 anos de idade: SENIOR
# Acima: MASTER

from datetime import date

anoatual = date.today().year
ano = int(input("Digite seu ano de nascimento: "))
idade = (anoatual - ano)

if idade <= 9:
    print("Você se encaixa na categoria MIRIM da equipe de natação!")
elif idade <= 14:
    print ("Você se encaixa na categoria INFANTIL da equipe de natação!")
elif idade <= 19:
    print ("Você se encaixa na categoria JUNIOR da equipe de natação!")
elif idade <= 25:
    print ("Você se encaixa na categoria SENIOR da equipe de natação!")
else:
    print ("Você se encaixa na categoria MASTER da equipe de natação!")