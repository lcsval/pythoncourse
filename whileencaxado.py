def fatorial(n):
    fatorial = 1
    while n > 1:
        fatorial = fatorial * n
        n = n -1
    return fatorial

n = int(input("Digite um número inteiro: "))
while n >= 0:
    print(fatorial(n))
    n = int(input("Digite um número inteiro: "))

