import re

def le_assinatura():
    '''A funcao le os valores dos tracos linguisticos do modelo e devolve uma assinatura a ser comparada com os textos fornecidos'''
    print("Bem-vindo ao detector automático de COH-PIAH.")
    print("Informe a assinatura típica de um aluno infectado:")

    wal = float(input("\nEntre o tamanho médio de palavra:"))
    ttr = float(input("Entre a relação Type-Token:"))
    hlr = float(input("Entre a Razão Hapax Legomana:"))
    sal = float(input("Entre o tamanho médio de sentença:"))
    sac = float(input("Entre a complexidade média da sentença:"))
    pal = float(input("Entre o tamanho medio de frase:"))

    return [wal, ttr, hlr, sal, sac, pal]

def le_textos():
    '''A funcao le todos os textos a serem comparados e devolve uma lista contendo cada texto como um elemento'''
    i = 1
    textos = []
    texto = input("Digite o texto " + str(i) +" (aperte enter para sair):")
    while texto:
        textos.append(texto)
        i += 1
        texto = input("Digite o texto " + str(i) +" (aperte enter para sair):")

    return textos

def separa_sentencas(texto):
    '''A funcao recebe um texto e devolve uma lista das sentencas dentro do texto'''
    sentencas = re.split(r'[.!?]+', texto)
    if sentencas[-1] == '':
        del sentencas[-1]
    return sentencas

def separa_frases(sentenca):
    '''A funcao recebe uma sentenca e devolve uma lista das frases dentro da sentenca'''
    return re.split(r'[,:;]+', sentenca)

def separa_palavras(frase):
    '''A funcao recebe uma frase e devolve uma lista das palavras dentro da frase'''
    return frase.split()

def n_palavras_unicas(lista_palavras):
    '''Essa funcao recebe uma lista de palavras e devolve o numero de palavras que aparecem uma unica vez'''
    freq = dict()
    unicas = 0
    for palavra in lista_palavras:
        p = palavra.lower()
        if p in freq:
            if freq[p] == 1:
                unicas -= 1
            freq[p] += 1
        else:
            freq[p] = 1
            unicas += 1

    return unicas

def n_palavras_diferentes(lista_palavras):
    '''Essa funcao recebe uma lista de palavras e devolve o numero de palavras diferentes utilizadas'''
    freq = dict()
    for palavra in lista_palavras:
        p = palavra.lower()
        if p in freq:
            freq[p] += 1
        else:
            freq[p] = 1

    return len(freq)

def compara_assinatura(as_a, as_b):
    '''IMPLEMENTAR. Essa funcao recebe duas assinaturas de texto e deve devolver o grau de similaridade nas assinaturas.'''
    pass

def calcula_assinatura(texto):
    '''IMPLEMENTAR. Essa funcao recebe um texto e deve devolver a assinatura do texto.'''

    palavras_separadas = separa_palavras(texto)
    t_medio = tamanho_medio(palavras_separadas)
    print("Tamanho médio: ", t_medio)

    t_token = type_token(palavras_separadas)
    print("Type Token: ", t_token)

    r_hapax_legomana = razao_hapax_legomana(palavras_separadas)
    print("Razao hapaxlegomana: ", r_hapax_legomana)

    t_medio_sentenca = tamanho_medio_sentenca(texto)
    print("Tamanho médio sentença: ", t_medio_sentenca)

    c_sentenca = len(separa_frases(texto)) / len(separa_sentencas(texto))
    print("Complexidade sentença: ", c_sentenca)

    t_medio_frase = tamanho_medio_frase(texto)
    print("Tamanho médio frase: ", tamanho_t_medio_fraseedio_frase)

    pass

def avalia_textos(textos, ass_cp):
    '''IMPLEMENTAR. Essa funcao recebe uma lista de textos e uma assinatura ass_cp e deve devolver o numero (1 a n) do texto com maior probabilidade de ter sido infectado por COH-PIAH.'''
    pass

def tamanho_medio(lista_palavras):
    return soma_tamanho_palavras(lista_palavras) / len(lista_palavras)

def soma_tamanho_palavras(lista_palavras):
    soma_tamanhos = 0
    for item in lista_palavras:
        soma_tamanhos = soma_tamanhos + len(item)
    return soma_tamanhos

def type_token(lista_palavras):
    return n_palavras_diferentes(lista_palavras) / len(lista_palavras)

def razao_hapax_legomana(lista_palavras):
    return n_palavras_unicas  (lista_palavras) / len(lista_palavras)

def tamanho_medio_sentenca(texto):
    sentencas = separa_sentencas(texto)

    soma = 0
    for sentenca in sentencas:
        sentencas_em_palavras = separa_palavras(sentenca)
        for palavra in sentencas_em_palavras:
            soma = soma + len(palavra)

    return soma / len(sentencas)

def tamanho_medio_frase(texto):
    frases = separa_frases(texto)

    soma = 0
    for frase in frases:
        frases_em_palavras = separa_palavras(frase)
        for palavra in frases_em_palavras:
            soma = soma + len(palavra)

    return soma / len(frases)
    

def main():
   assinatura = le_assinatura()
   print(assinatura)


##main()




print(calcula_assinatura("Muito além, nos confins inexplorados da região mais brega da Borda Ocidental desta Galáxia, há um pequeno sol amarelo e esquecido. Girando em torno deste sol, a uma distancia de cerca de 148 milhões de quilômetros, há um planetinha verde-azulado absolutamente insignificante, cujas formas de vida, descendentes de primatas, são tão extraordinariamente primitivas que ainda acham que relógios digitais são uma grande ideia."))