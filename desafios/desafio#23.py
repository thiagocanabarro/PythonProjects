#Faça um programa que leia um número de 0 a 9999 e mostre na tela cada dos dígitos separados
# ex : digite um número 1834: unidade: 4 dezena: 3 centena: 8 milhar: 1

n = int(input('Digite um número entre 0 e 9999: '))
n2 = str(int(10000 + n))
print('O número {} possui, {} milhares.'.format(n, n2[1]))
print('O número {} possui, {} centenas. '.format(n, n2[2]))
print('O número {} possui, {} dezenas. '.format(n, n2[3]))
print('O número {} possui, {} unidades.'.format(n, n2[4]))

# video aula

num = int(input("Digite um número de 0 a 9999: "))
# ex: digite o numero 1234. Esse número será dividido por 10. 1234/10 = 123,4. o resto da divisão será 4, que é a unidade do número 1234
u = num % 10
d = num // 10 % 10
c = num // 100 % 10
m = num // 1000
print("a unidade do número {} é {}".format(num,u))
print("a dezena do número {} é {}".format(num,d))
print("a centena do número {} é {}".format(num,c))
print("o milhar do número {} é {}".format(num,m))