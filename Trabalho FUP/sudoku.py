# Equipe: Carlos Alexandre, Jonathan Duarte, Helionardo Mendes | Sudoku #

# FUNCOES:

# Funcao feita para imprimir a tabela com seus respectivos valores:

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


# Funcao feita para ler os arquivos e transformar em variáveis:

def leitura(poj = bool(), string=''): #poj = Pistas(False) ou Jogadas(True) | string = jogada
    
    lista = list() 

    jogada_inv=False #Variável feita para retornar para a função principal se o jogador fez uma jogada válida ou não

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
        if i[0] in "AaBbCcDdEeFfGgHhIi":
            if i[0] in "Aa":
                col = 0
            elif i[0] in "Bb":
                col = 1
            elif i[0] in "Cc":
                col = 2
            elif i[0] in "Dd":
                col = 3
            elif i[0] in "Ee":
                col = 4
            elif i[0] in "Ff":
                col = 5
            elif i[0] in "Gg":
                col = 6
            elif i[0] in "Hh":
                col = 7
            elif i[0] in "Ii":
                col = 8
        else:
            if not poj:
              print(f'O programa foi encerrado por motivos de Pistas Inválidas.')
              exit()
            else:
              print("Jogada invalida! Por favor insira uma jogada valida.")
              jogada_inv = True
        
        if len(lista)<1 or len(lista)>80: #Verificando se o total de pistas está entre o intervalo [1;80]
            if not poj:
              print(f'O programa foi encerrado por motivos de Pistas Inválidas.')
              exit()
            else:
              print("Jogada invalida! Por favor insira uma jogada valida.")
              jogada_inv = True

        elif i[2] not in '123456789': #Verificando se o valor está entre 1 e 9
            if not poj:
              print(f'O programa foi encerrado por motivos de Pistas Inválidas.')
              exit()
            else:
              print("Jogada invalida! Por favor insira uma jogada valida.")
              jogada_inv = True
        
        elif i[1] not in '123456789': #Verificando se as linhas estão dentro as esperadas.
            if not poj:
              print(f'O programa foi encerrado por motivos de Pistas Inválidas.')
              exit()
            else:
              print("Jogada invalida! Por favor insira uma jogada valida.")
              jogada_inv = True

        lin = int(i[1])-1 #Adicionando valor para a linha
        val = int(i[2]) #Valor a ser adicionado na matriz

        if verificar(col, lin, val, sudoku, not poj): #Verifica se está valido
            add(col, lin, val, sudoku) #Adiciona na matriz
        
        else:  #Caso não esteja válido verá qual o motivo abaixo
          if not poj:
            print(f'O programa foi encerrado por motivos de Pistas Invalidas.')
            exit()
          else:
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

    return jogada_inv


# Funcao feita para adicionar os valores na tabela:

def add(col, lin, val, matriz = list()):
  matriz[col][lin] = val


# Funcao feita para verificar se os valores recebidos estão de acordo com as regras do sudoku:

def verificar(col, lin, val, matriz = list(), saopistas=True): 
    
    #saopistas será usado para quando rodar as pistas(False) elas não pararem na função pistasocupadas. True é quando não for as pistas

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


# -=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=- MAIN -=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=- #

# Inicializando a matriz:
sudoku = []
for i in range(9):
  linha = [" "]*9
  sudoku.append(linha)

posicaopistas = list() #Lista para salvar as posicoes das pistas 

pistaoujogada = False #Variável booleana criada para a funcao leitura em que irá ler ou os arquivos das pistas ou a string da jogada 
leitura(pistaoujogada)
pistaoujogada = True

jogada_invalida =  False #Variavel booleana criada para avisar quando a jogada for invalida e o jogador ter que digitar novamente sua jogada.

while not completa(sudoku):
  tabela(sudoku)
  jogada = input('\nDigite sua jogada: ')
  while leitura(pistaoujogada, jogada): #Enquanto a jogada for inválida ele irá repeti-la.
    jogada = input('\nDigite sua jogada novamente: ')

if completa(sudoku):
   print(f'VOCE GANHOU!!! Parabens!!!')