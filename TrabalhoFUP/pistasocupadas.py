# Funcao feita para verificar se a jogada está numa posicao em que uma pista ocupa.

def pistasocupadas(col, lin, lista = list()): 

    flag = 0

    for i in lista: #Transformando as letras das colunas em números para poder comparar depois
        if i[0] in "Aa":
            i[0] = 0
        elif i[0] in "Bb":
            i[0] = 1
        elif i[0] in "Cc":
            i[0] = 2
        elif i[0] in "Dd":
            i[0] = 3
        elif i[0] in "Ee":
            i[0] = 4
        elif i[0] in "Ff":
            i[0] = 5
        elif i[0] in "Gg":
            i[0] = 6
        elif i[0] in "Hh":
            i[0] = 7
        elif i[0] in "Ii":
            i[0] = 8

    for i in lista: #Comparando se a coluna e a linha estão em uma posição ocupada por uma pista
        if col == i[0] and lin == i[1]:
            flag = 1
    
    return flag