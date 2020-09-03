a = int(input("Digite o primeiro número inteiro: ")) #1, 1, 1, 3, 
b = int(input("Digite o segundo número inteiro: "))  #2, 1, 2, 2,
c = int(input("Digite o terceiro número inteiro: ")) #3, 1, 2, 1,

if a >= b or a >= c:
    print("não estão em ordem crescente")
elif a < b and a >= c:
    print("não estão em ordem crescente")
elif b >= c:
    print("não estão em ordem crescente")
elif a < b and b < c:
    print("crescente")