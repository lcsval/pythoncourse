largura = int(input("digite a largura: "))
altura = int(input("digite a altura: "))

l = 1
a = 1
while a <= altura:
    print("#", end="")
    while l < largura:
        if a == 1 or a == altura or l == largura-1:
            print("#", end="")
        else:
            print(" ", end="")
        l = l + 1
    print()
    l = 1
    a = a + 1