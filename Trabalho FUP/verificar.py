def verificar(col, lin, val, matriz = list()):

    flag = True #Flag para retornar se há algum erro ou não.

    # Verificacao se a posição na matriz já está ocupada:

    if matriz[col][lin] != " ":
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