import os

a = int(input("Digite o valor de a: "))
b = int(input("Digite o valor de b: "))

os.system('clear')

if (a == b):
  soma = a + b
  print("Os valores são iguais segue a soma: ",soma)
elif( a != b):
  mult = a * b
  print("Os valores são diferetens segue a multiplicação: ",mult)