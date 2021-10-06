# Ex : peça 2 números e mostre todas as operações aritméticas neles possiveis

n1 = int(input("Digite um primeiro valor: "))
n2 = int(input("Digite um segundo valor: "))
so = (n1+n2)
su = (n1-n2)
dv = (n1/n2)
mu = (n1*n2)
po = (n1**n2)
di = (n1//n2)
re = (n1%n2)
print("\n A soma dos seus números é {}"
       "\n a subtração dos seus números é {}"
       "\n a divisão dos seus números é {}"
       "\n a mulitiplicação dos seus números é {}"
       "\n a potencialização dos seus números é {}"
       "\n a divisão inteira dos seus números é {}"
       "\n o resto da divisão dos seus números é {}".format (so,su,dv,mu,po,di,re))