def computador_escolhe_jogada(n, m):
    if (n % (m+1)) > 0:
        print("\nO computador tirou", n % (m+1), "peça(s).")
        return n % (m+1)

    print("\nO computador tirou", m, "peça(s).")
    return m

def usuario_escolhe_jogada(n, m):
    valor = 0
    valor = int(input("\nQuantas peças você vai tirar? "))

    while (valor > 0 and valor > m):
        print("\nOops! Jogada inválida! Tente de novo.")
        valor = int(input("\nQuantas peças você vai tirar? "))

    return valor
      
def partida():
    qtde_n = int(input("\nQuantas peças? "))
    limite_m = int(input("Limite de peças por jogada? "))

    jogada = 0
    if (qtde_n % (limite_m+1)) > 0:
        print("\nComputador começa!")
        jogada = 1 #computador
    else:
        print("\nVocê começa!")
        jogada = 2 #jogador

    while (qtde_n > 0):
        if (jogada == 1):
            qtde_n = qtde_n - computador_escolhe_jogada(qtde_n, limite_m)

            if (qtde_n > 0):
                print("Agora restam", qtde_n, "peça(s) no tabuleiro.")

            if (qtde_n == 0):
                print("Fim do jogo! O computador ganhou!")
                return 1

            jogada = 2 #próxima jogada é do jogador
        else:
            usr_rm = usuario_escolhe_jogada(qtde_n, limite_m)
            qtde_n = qtde_n - usr_rm
            print("Voce tirou", usr_rm, "peça(s).")

            if (qtde_n > 0):
                print("Agora restam", qtde_n, "peça(s) no tabuleiro.")

            if (qtde_n == 0):
                print("Fim do jogo! Você ganhou!")
                return 2

            jogada = 1 #próxima jogada é do computador

def campeonato():
    contador = 1
    computador = 0
    voce = 0

    while (contador < 4):
        print("\n***** Rodada", contador, "****")
        if (partida() == 1):
            computador = computador + 1
        else:
            voce = voce + 1
        
        contador = contador + 1

    print("\n**** Final do campeonato! ****")
    print("\nPlacar: Você", voce, "X", computador, "Computador")


def main():
    print("Bem-vindo ao jogo do NIM! Escolha:")
    print("\n1 - para jogar uma partida isolada")

    escolha = int(input("2 - para jogar um campeonato "))
    while (escolha != 1 and escolha != 2):
        print("Selecione uma opção válida!")
        print("\nBem-vindo ao jogo do NIM! Escolha:")
        print("\n1 - para jogar uma partida isolada")
        escolha = int(input("2 - para jogar um campeonato "))

    if (escolha == 1):
        print("\nVocê escolheu uma partida!")
        partida()
    
    if (escolha == 2):
        print("\nVocê escolheu um campeonato!")
        campeonato()

main()