def leitura(poj = bool(), string=''): #poj = Pistas(False) ou Jogadas(True) | string = jogada
    
    lista = list() 

    jogada_inv=False #Variável feita para retornar para a função principal se o jogador fez uma jogada válida ou não

    if not poj:
      with open ('arq_01_cfg', 'r') as pistas: #Leitura do arquivo para uma lista de strings
          for i in pistas.readlines():
              varstring = i.replace(',','').replace(':','').replace(' ','').strip() #Tratamento das strings
              lista.append(varstring)

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

        if verificar(col, lin, val, sudoku): #Verifica se está valido
            add(col, lin, val, sudoku) #Adiciona na matriz
        
        else:  #Caso não esteja válido verá qual o motivo abaixo
          if not poj:
            print(f'O programa foi encerrado por motivos de Pistas Invalidas.')
            exit()
          else:
            if sudoku[col][lin] != " ":
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