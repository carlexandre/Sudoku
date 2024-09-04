# Equipe: Carlos Alexandre, Jonathan Duarte, Helionardo Mendes | Sudoku #

# FUNCOES:

# Funcao feita para imprimir a tabela com seus respectivos valores.

def tabela(matriz=list()):
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


# Funcao feita para ler os arquivos e transformar em variáveis.

def leitura(listarquivo=list()):
  with open ('arq_01_cfg.txt', 'r') as pistas:
    for linha in pistas:
      listarquivo.append(pistas.read())
  

# -=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=- MAIN -=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=- #

# Inicializando a matriz:
sudoku = []
for i in range(9):
  linha = [" "]*9
  sudoku.append(linha)

tabela(sudoku)


