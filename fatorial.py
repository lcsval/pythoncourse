n = int(input("Digite o valor de n:"))

if n == 0 or n == 1:
    print(1)
else:
    fat = 0
    while n > 1:
        if fat > 0:
            fat = fat * (n-1)
        else:
            fat = fat + n * (n-1)
        n = n-1

    print(fat)

