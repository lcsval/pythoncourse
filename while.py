qtde = int(input("Digite a quantidade de números da sequencia:"))
soma = 0

contador = 0
while contador < qtde:
    valor = int(input("Digite um valor:"))
    soma = soma + valor
    contador = contador + 1

print("A soma total:", soma)