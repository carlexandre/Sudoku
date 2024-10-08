# Equipe: Carlos Alexandre, Jonathan Duarte, Helionardo Mendes | Sudoku #

from sys import argv #Será usada para ver os argumentos, arquivos e separar os modos

import os

letracoluna = [''] #Variável criada para salvar a letra da coluna para usar nos prints

posicaopistas = list() #Lista para salvar as posicoes das pistas 

posicao_jogadas = list() #Lista para salvar as posicoes das jogadas no modo BATCH

mostrartabela = [True] #Variável para mostrar ou não a tabela

jogadas_invalidas = list() #Lista para salvar as jogadas invalidas no modo BATCH

modo_batch = [False] #Variavel para saber se quando for ler uma pista está no modo batch

frase = [False, ""] #Variavel criada para guardar frases para aparecer após a tabela

comandosbool = [False] #Variavel criada para avisar quando estiver pedindo quais sao os comandos do jogo

arquivopistas = argv[1]

if len(argv)==3:
    arquivobatch = argv[2]

# FUNCOES:

# Funcao feita para imprimir a tabela com seus respectivos valores:

def tabela(matriz=list()):
    print('\033[90m_'*105)
    print(f"""\033[34m                                                 _       _          
                                    ___ _   _  __| | ___ | | ___   _ 
                                   / __| | | |/ _` |/ _ \| |/ / | | |
                                   \__ \ |_| | (_| | (_) |   <| |_| |
                                   |___/\__,_|\__,_|\___/|_|\_\__,__|
                                                                 \033[0;37;40m""")
    
    print(f"                               {'A':>5}{'B':>4}{'C':>4}{'D':>5}{'E':>4}{'F':>4}{'G':>5}{'H':>4}{'I':>4}")
    print('                                ++---+---+---++---+---+---++---+---+---++ ')
    
    for i in range(1,4):
      print(f'                               {i}|| {matriz[0][i-1]} | {matriz[1][i-1]} | {matriz[2][i-1]} || {matriz[3][i-1]} | {matriz[4][i-1]} | {matriz[5][i-1]} || {matriz[6][i-1]} | {matriz[7][i-1]} | {matriz[8][i-1]} ||{i}')
      if i!=3:
        print('                                ++---+---+---++---+---+---++---+---+---++ ')
    print('                                ++===+===+===++===+===+===++===+===+===++ ')
    
    for i in range(4,7):
      print(f'                               {i}|| {matriz[0][i-1]} | {matriz[1][i-1]} | {matriz[2][i-1]} || {matriz[3][i-1]} | {matriz[4][i-1]} | {matriz[5][i-1]} || {matriz[6][i-1]} | {matriz[7][i-1]} | {matriz[8][i-1]} ||{i}')
      if i!=6:
        print('                                ++---+---+---++---+---+---++---+---+---++ ')
    print('                                ++===+===+===++===+===+===++===+===+===++ ')
    
    for i in range(7,10):
      print(f'                               {i}|| {matriz[0][i-1]} | {matriz[1][i-1]} | {matriz[2][i-1]} || {matriz[3][i-1]} | {matriz[4][i-1]} | {matriz[5][i-1]} || {matriz[6][i-1]} | {matriz[7][i-1]} | {matriz[8][i-1]} ||{i}')
      print('                                ++---+---+---++---+---+---++---+---+---++ ')
    print(f"                               {'A':>5}{'B':>4}{'C':>4}{'D':>5}{'E':>4}{'F':>4}{'G':>5}{'H':>4}{'I':>4}")


# Funcao feita para ler os arquivos e transformar em variáveis no MODO INTERATIVO e PISTAS:

def leituraIP(poj = bool(), string=''): #poj = Pistas(False) ou Jogadas(True) | string = jogada
    
    lista = list() 

    jogada_inv = False # Variável feita para retornar para a função principal se o jogador fez uma jogada válida ou não

    booldicasdelete = False # Variável para voltar o resultado da variável "jogada_inv" que vai ser usada como True para não percorrer a função inteira, e no final irá voltar a ser False.

    if not poj:
      with open (arquivopistas, 'r') as pistas: #Leitura do arquivo para uma lista de strings
          for i in pistas.readlines():
              varstring = i.replace(',','').replace(':','').replace(' ','').replace(';','').strip() #Tratamento das strings
              lista.append(varstring)
              posicaopistas.append(varstring)

    else:
      varstring = string.replace(',','').replace(':','').replace(' ','').replace(';','').strip() #Tratamento das strings
      lista.append(varstring)
      

    for i in lista:
        #Verificando se as colunas estão dentro das esperadas, caso não esteja o programa é encerrado.
        #Transformando as letras em números para adicionar na matriz.

        if len(i) != 3:
            if not poj:
                if modo_batch[0]:
                    print('Configuracao de dicas invalida.')
                    exit()
                else:
                    print(f'\033[31;40mO programa foi encerrado por motivos de Pistas Invalidas.\033[m')
                    exit()
            else:
              print("\033[31;40m\nJogada Invalida! Por favor insira uma jogada valida.\033[m")
              jogada_inv = True

        if not jogada_inv and poj and i[0] in "?!":
          a = 1
        else:
          a = 0

        if not jogada_inv and i[a] in "AaBbCcDdEeFfGgHhIi":
            
            letracoluna[0] = i[a].upper() #Salvar letra da coluna

            if i[a] in "Aa":
                col = 0
            elif i[a] in "Bb":
                col = 1
            elif i[a] in "Cc":
                col = 2
            elif i[a] in "Dd":
                col = 3
            elif i[a] in "Ee":
                col = 4
            elif i[a] in "Ff":
                col = 5
            elif i[a] in "Gg":
                col = 6
            elif i[a] in "Hh":
                col = 7
            elif i[a] in "Ii":
                col = 8

        else:
            if not poj:
                if modo_batch[0]:
                    print('Configuracao de dicas invalida.')
                    exit()
                else:
                    print(f'\033[31;40mO programa foi encerrado por motivos de Pistas Invalidas.\033[m')
                    exit()
            elif not jogada_inv:
              print("\033[31;40m\nJogada Invalida! Por favor insira uma jogada valida.\033[m")
              jogada_inv = True

        if not jogada_inv and poj and i[0] == "?":
            if dicas(col,int(i[2])-1, sudoku):
                jogada_inv = True
                booldicasdelete = False
            else:
                mostrartabela[0] = False
                jogada_inv = True
                booldicasdelete = True # Variável para voltar o resultado da variável "jogada_inv" que vai ser usada como True para não percorrer a função inteira, e no final irá voltar a ser False.

        elif not jogada_inv and poj and i[0] == "!":
            if pistasocupadas(col,int(i[2])-1, posicaopistas):
                print("\033[31;40m\nO espaco ja esta ocupado com uma pista e nao pode ser deletado. Digite uma nova jogada.\033[m")
                jogada_inv = True
            else:
                if sudoku[col][int(i[2])-1] != " ":
                    jogada_inv = True
                    booldicasdelete = True
                    frase[1] = f'Valor {sudoku[col][int(i[2])-1]} removido da posicao ({letracoluna[0]}, {i[2]})'
                    frase[0] = True
                    delete(col,int(i[2])-1, sudoku)
                    mostrartabela[0] = True
                    os.system("clear")
                else:
                    print(f'\033[31;40m\nO espaco não tem valor para ser deletado. Digite um valor para ele ou insira uma nova jogada.\033[m')
                    jogada_inv = True
        
        if not jogada_inv and len(lista)<1 or len(lista)>80: #Verificando se o total de pistas está entre o intervalo [1;80]
            if not poj:
                if modo_batch[0]:
                    print('Configuracao de dicas invalida.')
                    exit()
                else:
                    print(f'\033[31;40mO programa foi encerrado por motivos de Pistas Invalidas.\033[m')
                    exit()

        elif not jogada_inv and (i[2] not in '123456789' or i[1] not in '123456789'): #Verificando se o valor e as linhas estão entre 1 e 9
            if not poj:
                if modo_batch[0]:
                    print('Configuracao de dicas invalida.')
                    exit()
                else:
                    print(f'\033[31;40mO programa foi encerrado por motivos de Pistas Invalidas.\033[m')
                    exit()
            else:
              print("\033[31;40m\nJogada Invalida! Por favor insira uma jogada valida.\033[m")
              jogada_inv = True

        if not jogada_inv and not poj and pistasocupadas(col, int(i[1])-1, posicaopistas) and sudoku[col][int(i[1])-1]!=int(i[2]) and sudoku[col][int(i[1])-1]!=" ":
                if modo_batch[0]:
                    print('Configuracao de dicas invalida.')
                    exit()
                else:
                    print(f'\033[31;40mO programa foi encerrado por motivos de Pistas Invalidas.\033[m')
                    exit()

        if not jogada_inv:
            lin = int(i[1])-1 #Adicionando valor para a linha
            val = int(i[2]) #Valor a ser adicionado na matriz

            if verificar(col, lin, val, sudoku, not poj): #Verifica se está valido
                add(col, lin, val, sudoku) #Adiciona na matriz
                mostrartabela[0] = True
                os.system("clear")
                if poj:
                    frase[1] = f'Valor {val} adicionado na posicao ({letracoluna[0]}, {lin+1})'
                    frase[0] = True
        
            else:  #Caso não esteja válido verá qual o motivo abaixo
                if not poj:
                    if modo_batch[0]:
                        
                        print('Configuracao de dicas invalida.')
                        exit()
                    else:
                        print(f'\033[31;40mO programa foi encerrado por motivos de Pistas Invalidas.\033[m')
                        exit()
                else:
                    mt='' #Manter ou trocar o valor
                    if sudoku[col][lin] != " " and not pistasocupadas(col, lin, posicaopistas):
                        mt = '0'
                    while mt not in '12' and mt!='TROCAR' and mt!='MANTER':
                        print(f'\033[35m\nPosicao ja esta ocupada. Voce deseja manter o valor ou trocar pelo novo numero? [1] MANTER | [2] TROCAR \033[m')
                        mt = input('Sua resposta: ').upper().strip()
                    if mt == '2' or mt=='TROCAR':
                        if verificar(col, lin, val, sudoku, False, True):
                            add(col,lin,val,sudoku)
                            mostrartabela[0] = True
                            frase[1] = f'Valor {val} adicionado na posicao ({letracoluna[0]}, {lin+1})'
                            frase[0] = True
                            jogada_inv = False
                            os.system("clear")
                        else:
                            print("\033[31;40m\nJogada Invalida! Por favor insira uma jogada valida.\033[m")
                            jogada_inv = True
                    elif mt =='1' or mt == 'MANTER':
                        jogada_inv = False
                        os.system("clear")
                    else:
                        print("\033[31;40m\nJogada Invalida! Por favor insira uma jogada valida.\033[m")
                        jogada_inv = True
    
    if booldicasdelete:
        jogada_inv = False
    
    return jogada_inv


# Funcao feita para adicionar os valores na tabela:

def add(col, lin, val, matriz = list()):
  matriz[col][lin] = val


# Funcao feita para verificar se os valores recebidos estão de acordo com as regras do sudoku:

def verificar(col, lin, val, matriz = list(), saopistas=True, trocar=False): 
    
    #'saopistas' será usado para quando rodar as pistas(False) elas não pararem na função pistasocupadas. True é quando não for as pistas

    #Trocar para quando a pessoar quiser trocar, ele vai verificar se a posicao está valida e não se esta ocupada, pois ja sabemos que está

    flag = True #Flag para retornar se há algum erro(False) ou não(True).

    #Verificando se a posição na matriz é ocupada por uma pista:

    if pistasocupadas(col, lin, posicaopistas) and not saopistas:
       flag = False

    # Verificacao se a posição na matriz já está ocupada:
    if flag and matriz[col][lin] != " ":
        if modo_batch[0]==True and matriz[col][lin] == sudoku[col][lin]:
            flag = True
        elif not trocar:
            flag = False
        else:
            flag = True
    
    # Verificacao das linhas e colunas

    i=0
    while flag and i<9:
        if i!=lin and matriz[col][i] == val:
            flag = False
        i+=1

    i=0
    while flag and i<9:
        if i!=col and matriz[i][lin] == val:
            flag = False
        i+=1

    # Verificacao dos quadrantes

    i=0 #Contador para as colunas
    j=0 #Contador para as linhas

    # Verifica em que parte do quadrante l está na horizontal, isso irá ajudar no while abaixo.
    if lin>=0 and lin<=2:
        j = 0
    elif lin>=3 and lin<=5:
        j = 3
    elif lin>=6 and lin<=8:
        j = 6

    # Verifica em que parte do quadrante c está na vertical, isso irá ajudar no while abaixo.
    if col>=0 and col<=2:
        i = 0
    elif col>=3 and col<=5:
        i = 3
    elif col>=6 and col<=8:
        i = 6

    iinicial = i #Salvar as variáveis i e j
    jinicial = j

    while flag and i<iinicial+3:
        j = jinicial
        while flag and j<jinicial+3:
            if (i!=col or j!=lin) and matriz[i][j] == val:
                flag = False
            j+=1
        i+=1
      
    return flag


# Funcao para verificar se a tabela está completa ou não, para o jogo finalizar:

def completa(matriz = list()):
    i = j = 0
    flag = True
    while i<9 and flag:
        j=0
        while j<9 and flag:
            if matriz[i][j] == " ": #Se tiver alguma posição vazia na matriz a flag fica falsa e mostra que não está completa
                flag = False
            j+=1
        i+=1
    
    return flag


# Funcao feita para verificar se a jogada está numa posicao em que uma pista ocupa:

def pistasocupadas(col, lin, lista = list()): 

    flag = False

    c = int() #Variavel para receber valor da coluna no for abaixo

    i=0

    while not flag and i<len(lista): #Transformando as letras das colunas em números para poder comparar depois
        if lista[i][0] in "Aa":
            c = 0
        elif lista[i][0] in "Bb":
            c = 1
        elif lista[i][0] in "Cc":
            c = 2
        elif lista[i][0] in "Dd":
            c = 3
        elif lista[i][0] in "Ee":
            c = 4
        elif lista[i][0] in "Ff":
            c = 5
        elif lista[i][0] in "Gg":
            c = 6
        elif lista[i][0] in "Hh":
            c = 7
        elif lista[i][0] in "Ii":
            c = 8
        
        if col == c and lin == int(lista[i][1])-1: #Comparando se a coluna e a linha estão em uma posição ocupada por uma pista
            flag = True

        i+=1
        
    return flag


# Funcao feita para ver as dicas quando o jogador solicitar:

def dicas(col, lin, matriz = list()):
    numerosdisponiveis = list()

    ji = False #Caso dê jogada inválida (Dica em uma posição ocupada) será retornado para a função leitura que a jogada é inválida

    if matriz[col][lin] != " ":
        print(f'\033[31;40m\nPosicao ja ocupada! Digite uma nova jogada.\033[m')
        ji = True

    else:
        for i in range(1,10):
            if verificar(col, lin, i, matriz):
                numerosdisponiveis.append(i)
        
        if len(numerosdisponiveis) == 0:
            print('\033[31;40mNao ha nenhum valor para essa posição. Mude seu jogo deletando posicoes ja existentes.\033[m')
            ji = True

        else:
            print(f'\033[32m\nValores Disponiveis ({letracoluna[0]}, {lin+1}): ', end='')
            for i in numerosdisponiveis:
                if i == numerosdisponiveis[len(numerosdisponiveis)-1]:
                    print(f'{i}\033[m')
                else:
                    print(f'{i}, ', end="")

    return ji


#Funcao para quando o jogador querer deletar o valor de alguma posicao:

def delete (col, lin, matriz):
    matriz[col][lin] = ' '


#Funcao para fazer a leitura do modo BATCH:

def leiturabatch():

    lista_jogadas = list() #Lista para salvar as jogadas desse modo

    #VALIDACAO DAS JOGADAS NO MODO BATCH
    with open(arquivobatch) as jogadas:
        for i in jogadas.readlines():
            varstring = i.replace(',','').replace(':','').replace(' ','').replace(';','').replace('.','').replace('%','').replace('*','').replace('#','').strip()
            lista_jogadas.append(varstring)

    for i in lista_jogadas:
        
        jogada_inv = False #Verificar se a jogada ja foi invalida antes e não precisar percorrer o for todo.

        if len(i) != 3:
            jogadas_invalidas.append(i) #Invalida pois está oferecendo menos ou mais argumentos necessários
            jogada_inv = True

        if not jogada_inv and i[0] == "!":
          a = 1
        else:
          a = 0

        if not jogada_inv:
            if i[1] not in '123456789' or i[2] not in '987654321':
                jogada_inv = True
                jogadas_invalidas.append(i) #Invalida pois a linha ou o valor não estão no intervalo [1,9]

        if not jogada_inv:
            if i[a] in "AaBbCcDdEeFfGgHhIi":
                if i[a] in "Aa":
                    col = 0
                elif i[a] in "Bb":
                    col = 1
                elif i[a] in "Cc":
                    col = 2
                elif i[a] in "Dd":
                    col = 3
                elif i[a] in "Ee":
                    col = 4
                elif i[a] in "Ff":
                    col = 5
                elif i[a] in "Gg":
                    col = 6
                elif i[a] in "Hh":
                    col = 7
                elif i[a] in "Ii":
                    col = 8

                lin = int(i[1])-1 #Adicionando valor para a linha
                val = int(i[2]) #Valor a ser adicionado na matriz

            else:
                jogadas_invalidas.append(i) #Invalida pois a coluna não está no intervalo [A,I]
                jogada_inv = True

        if i[0] == '!':
            if pistasocupadas(col,lin, posicaopistas):
                jogadas_invalidas.append(i)
                jogada_inv = True #Invalida pois está querendo deletar uma pista inicial
            else:
                if sudoku[col][lin] != " ":
                    delete(col,lin, sudoku)
                else:
                    jogadas_invalidas.append(i)
                    jogada_inv = True #Invalida pois está querendo deletar um valor nulo

        if not jogada_inv:
            if verificar(col, lin, val, sudoku):
                add(col, lin, val, sudoku)

            else:
                jogadas_invalidas.append(i) #Invalida pois não está seguindo as regras do sudoku
                jogada_inv = True


#Funcao para mostrar o menu do modo interativo

def show_menu():

    comecar = False #So começará o jogo depois de digitar start

    print(f"""\033[0;36;40m
        .----------------.  .----------------.  .----------------.  .----------------.  .----------------.  .----------------. 
    | .--------------. || .--------------. || .--------------. || .--------------. || .--------------. || .--------------. |
    | |    _______   | || | _____  _____ | || |  ________    | || |     ____     | || |  ___  ____   | || | _____  _____ | |
    | |   /  ___  |  | || ||_   _||_   _|| || | |_   ___ `.  | || |   .'    `.   | || | |_  ||_  _|  | || ||_   _||_   _|| |
    | |  |  (__ \_|  | || |  | |    | |  | || |   | |   `. \ | || |  /  .--.  \  | || |   | |_/ /    | || |  | |    | |  | |
    | |   '.___`-.   | || |  | '    ' |  | || |   | |    | | | || |  | |    | |  | || |   |  __'.    | || |  | '    ' |  | |
    | |  |`\____) |  | || |   \ `--' /   | || |  _| |___.' / | || |  \  `--'  /  | || |  _| |  \ \_  | || |   \ `--' /   | |
    | |  |_______.'  | || |    `.__.'    | || | |________.'  | || |   `.____.'   | || | |____||____| | || |    `.__.'    | |
    | |              | || |              | || |              | || |              | || |              | || |              | |
    | '--------------' || '--------------' || '--------------' || '--------------' || '--------------' || '--------------' |
        '----------------'  '----------------'  '----------------'  '----------------'  '----------------'  '----------------' 
    \n\n\n\033[0;37;40m""")

    print(f"""\033[0;32;40m\t\t\t    _                     __                                                     
    \t\t\t   | \ o  _  o _|_  _    (_ _|_  _. ._ _|_   ._   _. ._ _.    o  _   _   _. ._ | 
    \t\t\t   |_/ | (_| |  |_ (/_   __) |_ (_| |   |_   |_) (_| | (_|    | (_) (_| (_| |  o 
    \t\t\t          _|                                 |               _|      _|          \n\n\n\033[0;37;40m""")
    print("\t\t\t\t\t    (1) Start | (2) Comandos")

    menu = input('\n\t\t\t\t\t     Sua Opcao: ').upper().strip()

    while menu != "START" and menu != "COMANDOS" and menu not in "12": #Só irá aceitar respostas sendo start ou comands, fora isso irá pedir novamente.
        menu = input('\n\t\t\t\t\t    \033[31;40m Opcao Invalida. Sua Opcao: \033[m').upper().strip()

    if menu == "START" or menu=='1':
        comecar = True
        os.system("clear")

    elif menu == "COMANDOS" or menu=='2':
        os.system("clear")
        if show_comandos(): #Se essa função for verdade quer dizer que o jogador escolheu iniciar o jogo na aba de comandos.
            comecar = True
        else:
            comecar = False

    return comecar


#Funcao para mostrar os comandos do sudoku

def show_comandos():
    print("""\033[1;36;40m .----------------.  .----------------.  .----------------.  .----------------.  .-----------------. .----------------.  .----------------.  .----------------. 
    | .--------------. || .--------------. || .--------------. || .--------------. || .--------------. || .--------------. || .--------------. || .--------------. |
    | |     ______   | || |     ____     | || | ____    ____ | || |      __      | || | ____  _____  | || |  ________    | || |     ____     | || |    _______   | |
    | |   .' ___  |  | || |   .'    `.   | || ||_   \  /   _|| || |     /  \     | || ||_   \|_   _| | || | |_   ___ `.  | || |   .'    `.   | || |   /  ___  |  | |
    | |  / .'   \_|  | || |  /  .--.  \  | || |  |   \/   |  | || |    / /\ \    | || |  |   \ | |   | || |   | |   `. \ | || |  /  .--.  \  | || |  |  (__ \_|  | |
    | |  | |         | || |  | |    | |  | || |  | |\  /| |  | || |   / ____ \   | || |  | |\ \| |   | || |   | |    | | | || |  | |    | |  | || |   '.___`-.   | |
    | |  \ `.___.'\  | || |  \  `--'  /  | || | _| |_\/_| |_ | || | _/ /    \ \_ | || | _| |_\   |_  | || |  _| |___.' / | || |  \  `--'  /  | || |  |`\____) |  | |
    | |   `._____.'  | || |   `.____.'   | || ||_____||_____|| || ||____|  |____|| || ||_____|\____| | || | |________.'  | || |   `.____.'   | || |  |_______.'  | |
    | |              | || |              | || |              | || |              | || |              | || |              | || |              | || |              | |
    | '--------------' || '--------------' || '--------------' || '--------------' || '--------------' || '--------------' || '--------------' || '--------------' |
    '----------------'  '----------------'  '----------------'  '----------------'  '----------------'  '----------------'  '----------------'  '----------------' \n\n\n\033[0;37;40m""")
    print(f'\t\t\t\t\t\t\t    \033[1;32;40mAjuda => ?Coluna(A-I), Linha(1-9)')
    print(f'\n\t\t\t\t\t\t\t   Deletar => !Coluna(A-I), Linha(1-9)')
    print(f'\n\t\t\t\t\t\t     Adicionar => Coluna(A-I), Linha(1-9): Valor(1-9)\033[0;37;40m')

    print('\n\n\n\t\t\t\t\t\t\t\t (0) MENU || (1) START => ', end='')

    resposta = input('')

    while resposta not in "01":
        resposta = input('\n\t\t\t\t\t\t\t       \033[31;40m Opcao Invalida. Sua Opcao: \033[m')
    
    if resposta == '1':
        comecar =  True #Iniciar Jogo
    else:
        comecar =  False #Volta para o Menu
    
    comandosbool[0] = True

    os.system('clear')

    return comecar

# -=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=- MAIN -=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=- #

# Inicializando a matriz:
sudoku = []
for i in range(9):
  linha = [" "]*9
  sudoku.append(linha)

if len(argv)==3:
    modo_batch[0] = True

pistaoujogada = False #Variável booleana criada para a funcao leitura em que irá ler ou os arquivos das pistas ou a string da jogada 
leituraIP(pistaoujogada)
pistaoujogada = True

if len(argv)==2:

    while not show_menu():
        if not comandosbool:
            os.system("clear")
        else:
            comandosbool[0] = False
    
    while not completa(sudoku):
        if mostrartabela[0]:
            tabela(sudoku)
            print('\033[90m_\033[m'*105)
            if frase[0]:
                print(f'\033[33m\n{frase[1]:^105}\033[m')
                frase[0] = False
        print('\033[90m_\033[m'*105)
        jogada = input('\nDigite sua jogada: ')
        while leituraIP(pistaoujogada, jogada): #Enquanto a jogada for inválida ele irá repeti-la.
            print('\033[90m_\033[m'*105)
            jogada = input('\nDigite sua jogada: ')

    tabela(sudoku)
    print('\033[90m_\033[m'*105)
    msg = 'YOU WIN!!!'
    print(f'\033[1;32;40m\n{msg:^105}\033[m')
    print('\033[90m_\033[m'*105)

elif len(argv)==3:

    leiturabatch()

    for i in jogadas_invalidas:
        if len(i) == 3:
            print(f'A jogada ({i[0].upper()}),({i[1]}) = {i[2]} eh invalida!')
        elif len(i)==2:
            print(f'A jogada ({i[0].upper()}),({i[1]}) =  eh invalida!')

    if completa(sudoku):
        print('A grade foi preenchida com sucesso!')
    else:
        print('A grade nao foi preenchida!')
        