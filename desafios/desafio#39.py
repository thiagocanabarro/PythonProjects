# Faça um programa que leia o ano de um nascimento de um jovem e informe, de acordo com sua idade:
# Se ele ainda vai se alistar ao serviço
# Se é a hora de se alistar
# Se ja passou do tempo do alistamento.

from datetime import date

anoatual = date.today().year

ano = int(input("Qual seu ano de nascimento? "))

idade = (anoatual - ano)

if idade > 18:
    print("Já passou o seu tempo de alistamento")
elif idade == 18:
    print ("Você deve se alistar este ano")
elif idade < 18:
    print ("Você não precisa se alistar esse ano")