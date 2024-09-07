# Funcao feita para ver as dicas quando o jogador pedir

def dicas(col, lin, matriz = list()):
    numerosdisponiveis = list()

    ji = False #Caso dê jogada inválida (Dica em uma posição ocupada) será retornado para a função leitura que a jogada é inválida

    if matriz[col][lin] != " ":
        print(f'Posicao ja ocupada! Digite uma nova jogada.')
        ji = True

    else:
        for i in range(1,10):
            if verificar(col, lin, i, matriz):
                numerosdisponiveis.append(i)
        
        if len(numerosdisponiveis) == 0:
            print('Nao ha nenhum valor para essa posição. Mude seu jogo deletando posicoes ja existentes.')
            ji = True

        else:
            print(f'\nValores Disponiveis ({letracoluna[0]}, {lin+1}): ', end='')
            for i in numerosdisponiveis:
                if i == numerosdisponiveis[len(numerosdisponiveis)-1]:
                    print(f'{i}')
                else:
                    print(f'{i}, ', end="")

    return ji