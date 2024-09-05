def leituraspistas():

    lista = list() 

    with open ('arq_01_cfg', 'r') as pistas: #Leitura do arquivo para uma lista de strings
          for i in pistas.readlines():
              varstring = i.replace(',','').replace(':','').replace(' ','').strip() #Tratamento das strings
              lista.append(varstring)
              posicaopistas.append(varstring) #Sendo usada como ponteiro para retornar valor para a principal
    
    for i in lista:
        if len(i) != 3:
            print(f'O programa foi encerrado por motivos de Pistas Inválidas.')
            exit()

        if len(lista)<1 or len(lista)>80: #Verificando se o total de pistas está entre o intervalo [1;80]
            print(f'O programa foi encerrado por motivos de Pistas Inválidas.')
            exit()
        
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
                print(f'O programa foi encerrado por motivos de Pistas Inválidas.')
                exit()
            
        if i[2] not in '123456789': #Verificando se o valor está entre 1 e 9
            print(f'O programa foi encerrado por motivos de Pistas Inválidas.')
            exit()

        if i[1] not in '123456789': #Verificando se as linhas estão dentro as esperadas.
            print(f'O programa foi encerrado por motivos de Pistas Inválidas.')
            exit()
        