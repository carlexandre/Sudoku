# Equipe: Carlos Alexandre, Jonathan Duarte, Helionardo Mendes | Sudoku #

# FUNCOES:

# Funcao feita para imprimir a tabela com seus respectivos valores:

from sys import argv #Será usada para ver os argumentos e separar os modos

def tabela(matriz=list()):
    print('''                   _       _          
     ___ _   _  __| | ___ | | ___   _ 
    / __| | | |/ _` |/ _ \| |/ / | | |
    \__ \ |_| | (_| | (_) |   <| |_| |
    |___/\__,_|\__,_|\___/|_|\_\__,__|
                                  ''')
    print(f"{'A':>5}{'B':>4}{'C':>4}{'D':>5}{'E':>4}{'F':>4}{'G':>5}{'H':>4}{'I':>4}")
    print(' ++---+---+---++---+---+---++---+---+---++ ')
    
    for i in range(1,4):
      print(f'{i}|| {matriz[0][i-1]} | {matriz[1][i-1]} | {matriz[2][i-1]} || {matriz[3][i-1]} | {matriz[4][i-1]} | {matriz[5][i-1]} || {matriz[6][i-1]} | {matriz[7][i-1]} | {matriz[8][i-1]} ||{i}')
      if i!=3:
        print(' ++---+---+---++---+---+---++---+---+---++ ')
    print(' ++===+===+===++===+===+===++===+===+===++ ')
    
    for i in range(4,7):
      print(f'{i}|| {matriz[0][i-1]} | {matriz[1][i-1]} | {matriz[2][i-1]} || {matriz[3][i-1]} | {matriz[4][i-1]} | {matriz[5][i-1]} || {matriz[6][i-1]} | {matriz[7][i-1]} | {matriz[8][i-1]} ||{i}')
      if i!=6:
        print(' ++---+---+---++---+---+---++---+---+---++ ')
    print(' ++===+===+===++===+===+===++===+===+===++ ')
    
    for i in range(7,10):
      print(f'{i}|| {matriz[0][i-1]} | {matriz[1][i-1]} | {matriz[2][i-1]} || {matriz[3][i-1]} | {matriz[4][i-1]} | {matriz[5][i-1]} || {matriz[6][i-1]} | {matriz[7][i-1]} | {matriz[8][i-1]} ||{i}')
      print(' ++---+---+---++---+---+---++---+---+---++ ')
    print(f"{'A':>5}{'B':>4}{'C':>4}{'D':>5}{'E':>4}{'F':>4}{'G':>5}{'H':>4}{'I':>4}")


# Funcao feita para ler os arquivos e transformar em variáveis no MODO INTERATIVO:

def leituraIP(poj = bool(), string=''): #poj = Pistas(False) ou Jogadas(True) | string = jogada
    
    lista = list() 

    jogada_inv = False # Variável feita para retornar para a função principal se o jogador fez uma jogada válida ou não

    booldicasdelete = False # Variável para voltar o resultado da variável "jogada_inv" que vai ser usada como True para não percorrer a função inteira, e no final irá voltar a ser False.

    if not poj:
      with open ('arq_01_cfg', 'r') as pistas: #Leitura do arquivo para uma lista de strings
          for i in pistas.readlines():
              varstring = i.replace(',','').replace(':','').replace(' ','').strip() #Tratamento das strings
              lista.append(varstring)
              posicaopistas.append(varstring)

    else:
      varstring = string.replace(',','').replace(':','').replace(' ','').strip() #Tratamento das strings
      lista.append(varstring)

    for i in lista:
        #Verificando se as colunas estão dentro das esperadas, caso não esteja o programa é encerrado.
        #Transformando as letras em números para adicionar na matriz.

        if len(i) != 3:
            if not poj:
              print(f'O programa foi encerrado por motivos de Pistas Inválidas.')
              exit()
            else:
              print("Jogada invalida! Por favor insira uma jogada valida.")
              jogada_inv = True

        if not jogada_inv and poj and i[0] in "?!":
          a = 1
        else:
          a = 0

        if not jogada_inv and i[a] in "AaBbCcDdEeFfGgHhIi":
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
              print(f'O programa foi encerrado por motivos de Pistas Inválidas.')
              exit()
            elif not jogada_inv:
              print("Jogada invalida! Por favor insira uma jogada valida.")
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
          if pistasocupadas(col,i[2], sudoku):
            print("O espaco ja esta ocupado com uma pista e nao pode ser deletado.")
          else:
             if not verificar(col,i[2], sudoku):
               delete(col,i[2], sudoku)
        
        if not jogada_inv and len(lista)<1 or len(lista)>80: #Verificando se o total de pistas está entre o intervalo [1;80]
            if not poj:
              print(f'O programa foi encerrado por motivos de Pistas Inválidas.')
              exit()
            else:
              print("Jogada invalida! Por favor insira uma jogada valida.")
              jogada_inv = True

        elif not jogada_inv and i[2] not in '123456789': #Verificando se o valor está entre 1 e 9
            if not poj:
              print(f'O programa foi encerrado por motivos de Pistas Inválidas.')
              exit()
            else:
              print("Jogada invalida! Por favor insira uma jogada valida.")
              jogada_inv = True
        
        elif not jogada_inv and i[1] not in '123456789': #Verificando se as linhas estão dentro as esperadas.
            if not poj:
              print(f'O programa foi encerrado por motivos de Pistas Inválidas.')
              exit()
            else:
              print("Jogada invalida! Por favor insira uma jogada valida.")
              jogada_inv = True

        if not jogada_inv:
            lin = int(i[1])-1 #Adicionando valor para a linha
            val = int(i[2]) #Valor a ser adicionado na matriz

            if verificar(col, lin, val, sudoku, not poj): #Verifica se está valido
                add(col, lin, val, sudoku) #Adiciona na matriz
        
            else:  #Caso não esteja válido verá qual o motivo abaixo
                if not poj:
                    print(f'O programa foi encerrado por motivos de Pistas Invalidas.')
                    exit()
                else:
                    mt=1
                    if sudoku[col][lin] != " " and not pistasocupadas(col, lin, posicaopistas):
                        mt = 0
                    while mt!=1 and mt!=2:
                        print(f'Posicao ja esta ocupada. Voce deseja manter o valor ou trocar pelo novo numero? [1] MANTER | [2] TROCAR ')
                        mt = int(input())
                    if mt == 2:
                        add(col,lin,val,sudoku)
                    else:
                        print("Jogada invalida! Por favor insira uma jogada valida.")
                        jogada_inv = True
    
    if booldicasdelete:
        jogada_inv = False
    
    return jogada_inv


# Funcao feita para adicionar os valores na tabela:

def add(col, lin, val, matriz = list()):
  matriz[col][lin] = val


# Funcao feita para verificar se os valores recebidos estão de acordo com as regras do sudoku:

def verificar(col, lin, val, matriz = list(), saopistas=True): 
    
    #'saopistas' será usado para quando rodar as pistas(False) elas não pararem na função pistasocupadas. True é quando não for as pistas

    flag = True #Flag para retornar se há algum erro(False) ou não(True).

    #Verificando se a posição na matriz é ocupada por uma pista:

    if pistasocupadas(col, lin, posicaopistas) and not saopistas:
       flag = False

    # Verificacao se a posição na matriz já está ocupada:
    if matriz[col][lin] != " " and flag:
        flag = False
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
        print(f'Posição já ocupada! Digite uma nova jogada.')
        ji = True

    else:
        for i in range(1,10):
            if verificar(col, lin, i, matriz):
                numerosdisponiveis.append(i)

        print(f'\nVALORES DISPONIVEIS: ', end='')
        for i in numerosdisponiveis:
            if i == numerosdisponiveis[len(numerosdisponiveis)-1]:
                print(f'{i}')
            else:
                print(f'{i}, ', end="")

    return ji


#Funcao para quando o jogador querer deletar o valor de alguma posicao:

def delete (col, lin, matriz):
    matriz[col][lin] = ' '

# -=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=- MAIN -=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=- #

# Inicializando a matriz:
sudoku = []
for i in range(9):
  linha = [" "]*9
  sudoku.append(linha)

posicaopistas = list() #Lista para salvar as posicoes das pistas 

pistaoujogada = False #Variável booleana criada para a funcao leitura em que irá ler ou os arquivos das pistas ou a string da jogada 
leituraIP(pistaoujogada)
pistaoujogada = True

jogada_invalida =  False #Variavel booleana criada para avisar quando a jogada for invalida e o jogador ter que digitar novamente sua jogada.

mostrartabela= [True] #Variável  para não mostrar tabela depois de usar dica

if len(argv)==1:
    while not completa(sudoku):
        if mostrartabela[0]:
            tabela(sudoku)
        jogada = input('\nDigite sua jogada: ')
        while leituraIP(pistaoujogada, jogada): #Enquanto a jogada for inválida ele irá repeti-la.
            jogada = input('\nDigite sua jogada novamente: ')

    if completa(sudoku):
        print(f'VOCE GANHOU!!! Parabens!!!')
    