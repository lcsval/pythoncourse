import math

n1 = float(input("Insira o valor de A: "))
n2 = float(input("Insira o valor de B: "))
n3 = float(input("Insira o valor de C: "))
n4 = float(input("Insira o valor de D: "))

a = (n1 - n2)**2 + (n3 - n4)**2
b = math.sqrt(a)

if b >= 10:
    print("longe")
else:
    print("perto")