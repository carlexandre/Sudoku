# Funcao feita para ver as dicas quando o jogador pedir

def dicas(col, lin, matriz = list()):
    numerosdisponiveis = list()

    for i in range(1,10):
        if verificar(col, lin, i, matriz):
            numerosdisponiveis.append(i)

    print(f'Valores Disponíveis para a posicao desejada: ', end='')
    for i in numerosdisponiveis:
        print(f'{i} ', end="")