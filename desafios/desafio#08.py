# Escreva um programa que leia um valor em metros e o exiba convertido em centimetros e milimetros

vm = int(input("Digite um valor em metros:"))

vcm = vm*100
vmm = vm*1000

print ("{} metros equivalem a: {} centimetros".format(vm,vcm))
print ("e {} equivalem também a: {} milimetros".format(vm,vmm))