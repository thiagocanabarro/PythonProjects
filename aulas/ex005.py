# Faça um programa que leia algo pelo teclado e mostre na tela o seu tipo primitivo e todas as informações possiveis sobre ele.

a = input ("Digite algo")
print ("o tipo primitivo desse valor é", type(a))
print ("Só tem espaços?", a.isspace())
print ("Só tem números?", a.isnumeric())
print ("É alfabético?", a.isalpha())
print ("É alfanumérico?", a.isalnum())
print ("Está em maiúsculas?", a.isupper())
print ("Está em minúsculas?", a.islower())
print ("Está capitalizada?", a.istitle())

