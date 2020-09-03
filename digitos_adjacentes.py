numeros = int(input("Digite um número inteiro: "))

contem = False
while numeros != 0:
    resto = numeros % 10
    diminuidor = numeros // 10

    teste = diminuidor % 10
    if resto == diminuidor % 10:
        contem = True

    numeros = diminuidor

if contem:
    print("sim")
else:
    print("não")
