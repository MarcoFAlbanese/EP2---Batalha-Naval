import random

#função para criar o mapa
def cria_mapa(n):
    listaf = [' '] * n
    mapa = []

    for e in range(n):
        mapa.append(list(listaf))  

    return mapa

#função para calcular se cabe o navio no mapa
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

#função para alocar randomicamente navios no mapa
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

# função de condição de vitoria
def foi_derrotado(matriz):
    for e in range (len(matriz)):
        if 'N' in matriz[e]:
            return False
    
    return True

# quantidade de blocos por modelo de navio
config = {
    'destroyer': 3,
    'porta-avioes': 5,
    'submarino': 2,
    'torpedeiro': 3,
    'cruzador': 2,
    'couracado': 4
}

# frotas de cada pais
paises =  {
    'Brasil': {
        'cruzador': 1,
        'torpedeiro': 2,
        'destroyer': 1,
        'couracado': 1,
        'porta-avioes': 1
    }, 
    'França': {
        'cruzador': 3, 
        'porta-avioes': 1, 
        'destroyer': 1, 
        'submarino': 1, 
        'couracado': 1
    },
    'Austrália': {
        'couracado': 1,
        'cruzador': 3, 
        'submarino': 1,
        'porta-avioes': 1, 
        'torpedeiro': 1
    },
    'Rússia': {
        'cruzador': 1,
        'porta-avioes': 1,
        'couracado': 2,
        'destroyer': 1,
        'submarino': 1
    },
    'Japão': {
        'torpedeiro': 2,
        'cruzador': 1,
        'destroyer': 2,
        'couracado': 1,
        'submarino': 1
    }
}

# alfabeto para montar o nome das colunas
alfabeto = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'

# cores para o terminal
cores = {
    'reset': '\u001b[0m',
    'red': '\u001b[31m',
    'black': '\u001b[30m',
    'green': '\u001b[32m',
    'yellow': '\u001b[33m',
    'blue': '\u001b[34m',
    'magenta': '\u001b[35m',
    'cyan': '\u001b[36m',
    'white': '\u001b[37m'
}
#print da introdução
print(" ============================ \n")
print("|                            | \n")
print ("| Bem-vindo ao batalha naval | \n")
print("|                            | \n")
print(" ============================ \n")


# loop para imprimir as frotas disponiveis
count = 0
dicPaises={}

for pais in paises:  
    print("{0}: {1} \n".format(count+1,pais))
    dicPaises[str(count+1)]=pais

    for barco in paises[pais]:
        print("     {0} {1}".format(paises[pais][barco],barco))
    
    print("\n")
    
    count += 1


# loop para checar se escholha é valida

numPaisEscolhido=input("\n Qual o número de nação da sua frota?")
print("\n")

if numPaisEscolhido not in dicPaises:
    print("Opção inválida")
    numPaisEscolhido=input("\n Qual o número de nação da sua frota?")
print(" Você escolheu a nação {0} \n".format(dicPaises[numPaisEscolhido]))
print("Agora é a sua vez de alocar seus navios de guerra!\n")
numPaisEscolhido = dicPaises[numPaisEscolhido]


#Lista para cada pais, cada argumento é o número de blocos e cada indice é um barco

lista_paises_frota = []
frotaEscolhida = paises[numPaisEscolhido]
for navio in frotaEscolhida:
    numNavios = frotaEscolhida[navio]
    for j in range(numNavios):
        lista_paises_frota.append(config[navio])

#print(lista_paises_frota)
#criação de mapa do computador
mapaFunc=aloca_navios(cria_mapa(10),lista_paises_frota)



#caracter bloco ▓

#impressão do mapa com numeros e letras

def imprime_mapa_com_numeros(mapa):
    letras_colunas = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J"]
    print("  " + " ".join(letras_colunas)) 
    for i, linha in enumerate(mapa):
        print(str(i) + " " + " ".join(linha))  

imprime_mapa_com_numeros(mapaFunc)