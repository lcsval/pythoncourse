valor = int(input("Digite um número inteiro:"))

unidade = valor % 10
numero = (valor - unidade)
divisao = numero // 10
dezena = divisao % 10

print("O dígito das dezenas é", dezena)