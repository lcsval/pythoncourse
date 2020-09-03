import math

a = float(input("Insira o valor de A: "))
b = float(input("Insira o valor de B: "))
c = float(input("Insira o valor de C: "))

x = (b ** 2)-(4 * a * c)

if x < 0:
    print("esta equação não possui raízes reais")
else:
    x = math.sqrt(x)

if x == 0:
    x1 = (-b + x) / (2 * a)
    print("a raiz desta equação é", x1)

if x > 0:
    x1 = (-b + x) / (2 * a)
    x2 = (-b - x) / (2 * a)
    if x1 > 0 and x2 > 0:
        print("as raízes da equação são", x1, "e", x2)
    else:
        print("as raízes da equação são", x2, "e", x1)

    