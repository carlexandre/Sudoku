listarquivo = list() #Parametros da Função

with open ('arq_01_cfg', 'r') as pistas: #Leitura do arquivo para uma lista de strings
    for i in pistas.readlines():
        varstring = i.replace(',','').replace(':','').replace(' ','').strip() #Tratamento das strings
        listarquivo.append(varstring)

for i in listarquivo:
    #Verificando se as colunas estão dentro das esperadas, caso não esteja o programa é encerrado.
    #Transformando as letras em números para manejamento das matrizes.
    if i[0] in "AaBbCcDdEeFfGgHhIi":
        if i[0] in "Aa":
            c = 0
        elif i[0] in "Bb":
            c = 1
        elif i[0] in "Cc":
            c = 2
        elif i[0] in "Dd":
            c = 3
        elif i[0] in "Ee":
            c = 4
        elif i[0] in "Ff":
            c = 5
        elif i[0] in "Gg":
            c = 6
        elif i[0] in "Hh":
            c = 7
        elif i[0] in "Ii":
            c = 8
    else:
        print(f'O programa foi encerrado por motivos de Pistas Inválidas.')
        SystemExit
    
    l = i[1] #Adicionando valor para a linha
    v = i[2] #Valor a ser adicionado
    
