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
                    print(f'O programa foi encerrado por motivos de Pistas Invalidas.')
                    exit()
            else:
              print("\nJogada Invalida! Por favor insira uma jogada valida.")
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
                    print(f'O programa foi encerrado por motivos de Pistas Invalidas.')
                    exit()
            elif not jogada_inv:
              print("\nJogada Invalida! Por favor insira uma jogada valida.")
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
                print("\nO espaco ja esta ocupado com uma pista e nao pode ser deletado. Digite uma nova jogada.")
                jogada_inv = True
            else:
                if sudoku[col][int(i[2])-1] != " ":
                    jogada_inv = True
                    booldicasdelete = True
                    print(f'\nValor {sudoku[col][int(i[2])-1]} removido da posicao ({letracoluna[0]}, {i[2]})')
                    delete(col,int(i[2])-1, sudoku)
                else:
                    print(f'\nO espaco não tem valor para ser deletado. Digite um valor para ele ou insira uma nova jogada.')
                    jogada_inv = True
        
        if not jogada_inv and len(lista)<1 or len(lista)>80: #Verificando se o total de pistas está entre o intervalo [1;80]
            if not poj:
                if modo_batch[0]:
                    print('Configuracao de dicas invalida.')
                    exit()
                else:
                    print(f'O programa foi encerrado por motivos de Pistas Invalidas.')
                    exit()

        elif not jogada_inv and (i[2] not in '123456789' or i[1] not in '123456789'): #Verificando se o valor e as linhas estão entre 1 e 9
            if not poj:
                if modo_batch[0]:
                    print('Configuracao de dicas invalida.')
                    exit()
                else:
                    print(f'O programa foi encerrado por motivos de Pistas Invalidas.')
                    exit()
            else:
              print("\nJogada Invalida! Por favor insira uma jogada valida.")
              jogada_inv = True

        if not jogada_inv and not poj and pistasocupadas(col, int(i[1])-1, posicaopistas) and sudoku[col][int(i[1])-1]!=int(i[2]) and sudoku[col][int(i[1])-1]!=" ":
                print('Configuracao de dicas invalida.')
                exit()

        if not jogada_inv:
            lin = int(i[1])-1 #Adicionando valor para a linha
            val = int(i[2]) #Valor a ser adicionado na matriz

            if verificar(col, lin, val, sudoku, not poj): #Verifica se está valido
                add(col, lin, val, sudoku) #Adiciona na matriz
                mostrartabela[0] = True
                if poj:
                    print(f'\nValor {val} adicionado na posicao ({letracoluna[0]}, {lin+1})')
        
            else:  #Caso não esteja válido verá qual o motivo abaixo
                if not poj:
                    if modo_batch[0]:
                        print('Configuracao de dicas invalida.')
                        exit()
                    else:
                        print(f'O programa foi encerrado por motivos de Pistas Invalidas.')
                        exit()
                else:
                    mt=1
                    if sudoku[col][lin] != " " and not pistasocupadas(col, lin, posicaopistas):
                        mt = 0
                    while mt!=1 and mt!=2:
                        print(f'\nPosicao ja esta ocupada. Voce deseja manter o valor ou trocar pelo novo numero? [1] MANTER | [2] TROCAR ')
                        mt = int(input('Sua resposta: '))
                    if mt == 2:
                        if verificar(col, lin, val, sudoku):
                            add(col,lin,val,sudoku)
                        else:
                            jogada_inv = True
                    else:
                        print("\nJogada Invalida! Por favor insira uma jogada valida.")
                        jogada_inv = True
    
    if booldicasdelete:
        jogada_inv = False
    
    return jogada_inv
