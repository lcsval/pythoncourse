lista = []
x = 1
while x > 0:
    valor = int(input("Digite um número: "))
    if (valor != 0):
        lista.append(valor)
    x = valor


print(sorted(lista, reverse=True))