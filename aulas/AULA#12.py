nome = str(input("Qual é seu nome")).lower().strip()

if nome == "gustavo":
    print("Que nome bonito")
elif nome == "pedro" or nome == "maria" or nome == "joão":
    print ("O seu nome é bem popular")
elif nome == "ana katarina":
    print ("que nome feio")
else:
    print("Seu nome é bem chato")
