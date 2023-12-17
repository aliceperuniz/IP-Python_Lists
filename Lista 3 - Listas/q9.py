matriz = []
n_linhas_matriz = int(input())
maior_soma_linhas = -1
maior_soma_colunas = -1
maior_soma_diagonal = -1
maior_dupla_linhas = list()
maior_dupla_colunas = list()
maior_dupla_diagonal = list()
for i in range(n_linhas_matriz):
  linha_n = input().split(" ")
  matriz.append(linha_n)
for linha in range(0, n_linhas_matriz):
  for coluna in range(0, n_linhas_matriz-1):
    if int(matriz[linha][coluna]) + int(matriz[linha][coluna + 1]) > maior_soma_linhas:
      maior_soma_linhas = int(matriz[linha][coluna]) + int(matriz[linha][coluna + 1])
      maior_dupla_linhas = [matriz[linha][coluna], matriz[linha][coluna + 1]]
    if int(matriz[coluna][linha]) + int(matriz[coluna + 1][linha]) > maior_soma_colunas:
      maior_soma_colunas = int(matriz[coluna][linha]) + int(matriz[coluna + 1][linha])
      maior_dupla_colunas = [matriz[coluna][linha], matriz[coluna + 1][linha]]
for diagonal in range(0, n_linhas_matriz-1):
  if int(matriz[diagonal][diagonal]) + int(matriz[diagonal + 1][diagonal + 1]) > maior_soma_diagonal:
    maior_soma_diagonal = int(matriz[diagonal][diagonal]) + int(matriz[diagonal + 1][diagonal + 1])
    maior_dupla_diagonal = [matriz[diagonal][diagonal], matriz[diagonal + 1][diagonal + 1]]
senha = str(maior_dupla_linhas[0]) + str(maior_dupla_linhas[1]) + str(maior_dupla_colunas[0]) + str(maior_dupla_colunas[1]) + str(maior_dupla_diagonal[0]) + str(maior_dupla_diagonal[1])
print("Falei que era fácil Dustinzinho...")
print("Pegando todas os números que formam as combinações dos pares de cada sentido temos...")
print(f'Password: {senha}')
