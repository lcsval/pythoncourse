def remove_repetidos(lista):
    retorno = []
    for item in lista:
        if not item in retorno:
            retorno.append(item)
    
    return sorted(retorno)