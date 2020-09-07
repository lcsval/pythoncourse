def primo(x):
    fator = 2
    if (x == 2):
        return True
        
    while x % fator != 0 and fator <= x/2:
        fator = fator + 1

    if  x % fator == 0:
        return False
    else:
        return True

def n_primos(x):
    qtde = 0
    contador = x
    while contador > 1:
        if primo(contador):
            qtde = qtde + 1

        contador = contador - 1

    return qtde