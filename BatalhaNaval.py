import random

def cria_mapa(n):
    listaf = [' '] * n
    mapa = []

    for e in range(n):
        mapa.append(list(listaf))  

    return mapa

def posicao_suporta(mapa, blocos, linha, coluna, orientacao):
    
    if orientacao == "h":
        for i in range(blocos):
            if coluna + i >= len(mapa[linha]):
                return False
            elif mapa[linha][coluna + i] == "N":
                return False

    elif orientacao == "v":
        for i in range(blocos):
            if linha + i >= len(mapa):
                return False
            elif mapa[linha + i][coluna] == "N":
                return False
    return True

def aloca_navios(mapa,lista):
    numlinha = len(mapa)
    numcol = len(mapa[0])
    linha = random.randint(0, numlinha-1)
    coluna = random.randint(0, numcol-1)
    orientacao = random.choice(['h', 'v'])

    for navio in lista:
        resp = posicao_suporta(mapa, navio, linha, coluna, orientacao)

        while resp == False:
            linha = random.randint(0, numlinha-1)
            coluna = random.randint(0, numcol-1)
            orientacao = random.choice(['h', 'v'])
            resp = posicao_suporta(mapa, navio, linha, coluna, orientacao)

        if (orientacao == "v"):
            for l in range(navio):
                mapa[linha+l][coluna] = "N"
        elif (orientacao == "h"):
            for l in range(navio):
                mapa[linha][coluna+l] = "N"

    return (mapa)