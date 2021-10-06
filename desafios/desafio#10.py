# Crie um programa que leia quanto dinheiro uma pessoa tem na carteira e mostre quantos dólares ela pode comprar

real = float(input("Quantos reais você possui R$"))

dolar = real / 3.27

print('COM R${:.2f} você pode comprar US${:.2f}'.format(real,dolar))


