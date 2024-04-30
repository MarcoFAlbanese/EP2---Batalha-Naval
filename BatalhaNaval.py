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

#impressão do mapa com numeros e letras
def imprime_mapa_com_numeros(mapa):
    letras_colunas = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J"]
    print("   " + " ".join(letras_colunas)) 
    for i, linha in enumerate(mapa):
        numero_linha = str(i + 1)
        espacos = " " * (2 - len(numero_linha))
        if len(numero_linha) != 1:
            espacos = ""
        print(espacos + numero_linha + " " + " ".join(linha))

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

relacao_coluna_num = {"a":0,"b":1,"c":2,"d":3,"e":4,"f":5,"g":6,"h":7,"i":8,"j":9}


#criar dicionario com todos os paises e suas frotas como bloquinhos
dic_pais_frota={}
         
for pais in paises:
    if pais not in dic_pais_frota:
        lista_blocos = []
        lista_paises_frota = []
        frotaEscolhida = paises[pais]
        for navio in frotaEscolhida:
            numNavios = frotaEscolhida[navio]
            lista_blocos.append(numNavios)
            for j in range(numNavios):
                lista_paises_frota.append(config[navio])
            dic_pais_frota[pais] = lista_paises_frota

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

while numPaisEscolhido not in dicPaises:
    print("Opção inválida")
    numPaisEscolhido=input("\n Qual o número de nação da sua frota?")
print(" Você escolheu a nação {0} \n".format(dicPaises[numPaisEscolhido]))
print("Agora é a sua vez de alocar seus navios de guerra!\n")
nomePaisEscolhido = dicPaises[numPaisEscolhido]


#Lista para cada pais, cada argumento é o número de blocos e cada indice é um barco
aleatorioUser = input("Deseja alocar aleatoriamente a sua frota? Sim ou Não?")
aleatorioUserLower = aleatorioUser.lower()
lista_blocos=[]

if (aleatorioUserLower== "sim"):
    lista_paises_frota = []
    frotaEscolhida = paises[nomePaisEscolhido]
    for navio in frotaEscolhida:
        numNavios = frotaEscolhida[navio]
        lista_blocos.append(numNavios)
        for j in range(numNavios):
            lista_paises_frota.append(config[navio])
    mapa_jogador=aloca_navios(cria_mapa(10),lista_paises_frota)
    imprime_mapa_com_numeros(mapa_jogador)

else:
    mapa_jogador=cria_mapa(10)
    lista_paises_frota=[]
    frotaEscolhida = paises[nomePaisEscolhido]
    
    imprime_mapa_com_numeros(mapa_jogador)

    for navio in frotaEscolhida:
        numNavios = frotaEscolhida[navio]
        numBlocos = config[navio]
        for i in range(numNavios):
            lista_blocos.append(numBlocos)
    
    
    for navio in lista_blocos:
        coluna_escolhida = input("Informe a letra da coluna (A-J): ").lower()
        linha_escolhida = int(input("Informe o número da linha (1-10): ")) - 1  
        orientacao_escolhida = input("Informe a orientação [v|h]: ").lower()

        coluna_escolhida_num = relacao_coluna_num.get(coluna_escolhida, -1)  

        
        if coluna_escolhida_num == -1 or linha_escolhida < 0 or linha_escolhida >= len(mapa_jogador):
            print("Coordenadas inválidas! Por favor, escolha uma letra de coluna entre A e J e um número de linha entre 1 e 10.")
            continue
        if orientacao_escolhida not in ['v', 'h']:
            print("Orientação inválida! Por favor, escolha 'v' para vertical ou 'h' para horizontal.")
            continue
        if not posicao_suporta(mapa_jogador, navio, linha_escolhida, coluna_escolhida_num, orientacao_escolhida):
            print("Navio não cabe nesta posição. Escolha outra posição.")
            continue

        # Coloca o navio no mapa
        if orientacao_escolhida == "v":
            for l in range(navio):
                mapa_jogador[linha_escolhida + l][coluna_escolhida_num] = "\u001b[32m▓\u001b[37m"
        elif orientacao_escolhida == "h":
            for l in range(navio):
                mapa_jogador[linha_escolhida][coluna_escolhida_num + l] = "\u001b[32m▓\u001b[37m"

        imprime_mapa_com_numeros(mapa_jogador)

pais_jogador=dicPaises[numPaisEscolhido]
del dic_pais_frota[pais_jogador]

pais_comp=random.choice(list(dic_pais_frota.keys()))
frota_comp=dic_pais_frota[pais_comp]
mapa_comp = aloca_navios(cria_mapa(10),frota_comp)
print(frota_comp)
print(pais_comp)
print("\n")
imprime_mapa_com_numeros(mapa_comp)


mapa_show_comp=cria_mapa(10)
mapa_show_jog=cria_mapa(10)
#caracter bloco ▓

#rodada jogador

lista_posicoes_coluna=['a','b','c','d','e','f','h','i','j']
lista_posicoes_linha=[0,1,2,3,4,5,6,7,8,9]

while (foi_derrotado(mapa_comp)==False) or (foi_derrotado(mapa_jogador)==False):

    coluna_palpite  = input("Informe a letra da coluna (A-J): ").lower()
    linha_palpite = int(input("Informe o número da linha (1-10): ")) - 1  
    
    

    while (coluna_palpite not in lista_posicoes_coluna) or (linha_palpite not in lista_posicoes_linha):
            print("Coordenadas inválidas! Por favor, escolha uma letra de coluna entre A e J e um número de linha entre 1 e 10.")
            coluna_palpite  = input("Informe a letra da coluna (A-J): ").lower()
            linha_palpite = int(input("Informe o número da linha (1-10): ")) - 1  
            coluna_palpite_num=relacao_coluna_num.get(coluna_palpite)

    coluna_palpite_num=relacao_coluna_num.get(coluna_palpite)

    if (mapa_comp[linha_palpite][coluna_palpite_num]=="N"):
        mapa_comp[linha_palpite][coluna_palpite_num]="A"
        mapa_show_comp[linha_palpite][coluna_palpite_num]="\u001b[31m▓\u001b[37m"
    
    elif (mapa_comp[linha_palpite][coluna_palpite_num]=="A"):
        print("Você já fez um chute nessa posição, escolha outra")
        
        while (mapa_comp[linha_palpite][coluna_palpite_num]=="A"):
            
            coluna_palpite  = input("Informe a letra da coluna (A-J): ").lower()
            linha_palpite = int(input("Informe o número da linha (1-10): ")) - 1  
            coluna_palpite_num=relacao_coluna_num.get(coluna_palpite)
            

    elif (mapa_comp[linha_palpite][coluna_palpite_num] == " "):
        mapa_comp[linha_palpite][coluna_palpite_num]="A"
        mapa_show_comp[linha_palpite][coluna_palpite_num]="\u001b[34m▓\u001b[37m"

    else:
        mapa_show_comp[linha_palpite][coluna_palpite_num]="\u001b[34m▓\u001b[37m"
    imprime_mapa_com_numeros(mapa_show_comp)

    if (foi_derrotado(mapa_comp)==True):
        break
    
#rodada computador

    coluna_palpite_comp  = random.randint(0,9)
    linha_palpite_comp = random.randint(0,9)

    if coluna_palpite_comp == -1 or linha_palpite_comp < 0 or linha_palpite_comp >= len(mapa_jogador):
            print("Coordenadas inválidas! Por favor, escolha uma letra de coluna entre A e J e um número de linha entre 1 e 10.")
   
    if (mapa_jogador[linha_palpite_comp][coluna_palpite_comp]=="N"):
        mapa_jogador[linha_palpite_comp][coluna_palpite_comp]="A"
        mapa_show_jog[linha_palpite_comp][coluna_palpite_comp]="\u001b[31m▓\u001b[37m"
    
    elif (mapa_comp[linha_palpite_comp][coluna_palpite_comp]=="A"):
        print("Você já fez um chute nessa posição, escolha outra")


    elif (mapa_jogador[linha_palpite_comp][coluna_palpite_comp] == " "):
        mapa_jogador[linha_palpite_comp][coluna_palpite_comp]="A"
        mapa_show_jog[linha_palpite_comp][coluna_palpite_comp]="\u001b[34m▓\u001b[37m"

    else:
        mapa_show_jog[linha_palpite_comp][coluna_palpite_comp]="\u001b[34m▓\u001b[37m"
    imprime_mapa_com_numeros(mapa_show_jog)
    imprime_mapa_com_numeros(mapa_comp)



if (foi_derrotado(mapa_comp) == True):
    print("\u001b[32m Parabéns, você venceu!\u001b[37m")    
elif (foi_derrotado(mapa_jogador) == True):
    print("\u001b[31m Que pena, você perdeu!\u001b[37m")


