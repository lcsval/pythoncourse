valor = input("Digite um valor:")

soma = 0
i = 0
while i < len(valor):
    soma = soma + int(valor[i])
    i = i + 1

print(soma)