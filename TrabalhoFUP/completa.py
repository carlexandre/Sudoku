# Funcao para verificar se a tabela está completa ou não, para o jogo finalizar.

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


sudoku = []
for i in range(9):
  linha = [1]*9
  sudoku.append(linha)

sudoku[2][5] = " "

while not completa(sudoku):
    print('nao completa')

if completa(sudoku):
   print(f'VOCE GANHOU!!! Parabens!!!')