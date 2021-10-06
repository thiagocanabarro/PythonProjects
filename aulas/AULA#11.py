nome = str(input("Digite seu nome: "))

a = 3
b = 5

print ("Os valores são \33[1:31m{}\33[m e \33[1:31m{}\033[m".format(a,b))

cores = {"normal":"\33[m",
         "azul":"\33[34m",
         "amarelo":"\33[33m",
         "vermelho":"\33[41m",
         "roxo":"\33[35m",
         "pretoebranco":"\33[7:30m",
         "verde":"\33[32m",
         "ciano":"\33[36m",
         "cinza":"\33[37m",}


print ("Olá muito prazer {}{}{} !!! ".format(cores["ciano"], nome, cores["normal"]))