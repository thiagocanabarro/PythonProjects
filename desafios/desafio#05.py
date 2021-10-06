#Faça um programa que leia um número inteiro e mostre na tela o seu sucessor e seu antecessor

cores = {"normal":"\33[m",
         "azul":"\33[34m",
         "amarelo":"\33[33m",
         "vermelho":"\33[41m",
         "roxo":"\33[35m",
         "pretoebranco":"\33[7:30m",
         "verde":"\33[32m",
         "ciano":"\33[36m",
         "cinza":"\33[37m",}

n = int(input("Digite um número:"))
a = n-1
s = n+1
print ("O antecessor do número {}{} {}é {}{} {}e o sucessor dele é {}{}".format(cores["ciano"],n,
                                                                              cores["normal"],
                                                                              cores["azul"],a,
                                                                              cores["normal"],
                                                                              cores["roxo"],s))