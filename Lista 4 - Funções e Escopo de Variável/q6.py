def tipo_da_operacao(operacao):
  #descobriremos o tipo de operação a ser feita:
  
  global inteiro_k  #número inteiro existente na multiplicacao_escalar
  inteiro_k = int()
  global tipo_operacao
  global elemento_1 #elemento a ser somado ou subtraído ou multiplicado pelo elemento 2
  global elemento_2
  global matriz_multiplicada
  matriz_multiplicada = str()
  operacao = operacao.split(" ")
  elemento_1 = operacao[0]
  elemento_2 = operacao[2]
  sinal_operacao = operacao[1]
  

  if sinal_operacao == "*":
    tipo_operacao = "multiplicacao escalar"
    if elemento_1 == "m1":
      elemento_1 = matriz_1
      matriz_multiplicada = matriz_1
      inteiro_k = int(elemento_2)
    elif elemento_1 == "m2":
      elemento_1 = matriz_2
      matriz_multiplicada = matriz_2
      inteiro_k = int(elemento_2)
    if elemento_2 == "m1":
      elemento_2 = matriz_1
      matriz_multiplicada = matriz_1
      inteiro_k = int(elemento_1)
    elif elemento_2 == "m2":
      elemento_2 = matriz_2
      matriz_multiplicada = matriz_2
      inteiro_k = int(elemento_1)

  
  else:
    if elemento_1 == "m1":
      elemento_1 = matriz_1
    elif elemento_1 == "m2":
      elemento_1 = matriz_2
    if elemento_2 == "m1":
      elemento_2 = matriz_1
    elif elemento_2 == "m2":
      elemento_2 = matriz_2
    if sinal_operacao == ".":
      tipo_operacao = "multiplicacao"
    elif sinal_operacao == "+":
      tipo_operacao = "soma"
    elif sinal_operacao == "-":
      tipo_operacao = "subtracao"


def operacao_soma(x, y):
  
  
  resultado_temp = []
  global resultado
  resultado = []
  global matriz_1
  global matriz_2
  global matriz_resultado

  for linha_soma in range(0, len(x)):
    for coluna_soma in range(0, len(x)):
      resultado_temp.append(int(x[linha_soma][coluna_soma]) + int(y[linha_soma][coluna_soma]))
    resultado.append(resultado_temp)  
    resultado_temp = []

  if matriz_resultado == "m2":
    matriz_2 = resultado
  elif matriz_resultado == "m1":
    matriz_1 = resultado


def operacao_subtracao(x, y):
  
  
  resultado_temp = []
  global resultado
  resultado = []
  global matriz_1
  global matriz_2
  global matriz_resultado

  for linha_sub in range(0, len(x)):
    for coluna_sub in range(0, len(x)):
      resultado_temp.append(int(x[linha_sub][coluna_sub]) - int(y[linha_sub][coluna_sub]))
    resultado.append(resultado_temp) 
    resultado_temp = []

  if matriz_resultado == "m2":
    matriz_2 = resultado
  elif matriz_resultado == "m1":
    matriz_1 = resultado


def operacao_multiplicacao_matrizes(x, y):
  
  
  resultado_temp_elemento = []
  global resultado
  resultado = []
  global matriz_1
  global matriz_2
  global matriz_resultado
  soma = 0
  resultado_temp_total = []
  resultado_temp_total = []
  elementos_cada_linha = []
  
  for linhas_colunas_resultado in range(0, len(x)):
    for linha_do_resultado in range(0, len(x)):
      for i in range(0, len(x)):
        soma += int(elemento_1[linhas_colunas_resultado][i]) * int(elemento_2[i][linha_do_resultado])
      elementos_cada_linha.append(soma)
      soma = 0
    resultado_temp_total.append(elementos_cada_linha)
    elementos_cada_linha = []
  resultado = resultado_temp_total
  

  if matriz_resultado == "m2":
    matriz_2 = resultado
  elif matriz_resultado == "m1":
    matriz_1 = resultado


def operacao_multiplicacao_escalar(x, y):
  # Vamos multiplicar x(inteiro_k) por cada elemento de y(matriz_multiplicada)
  
  global resultado
  resultado = []
  linha_temp = []
  global matriz_resultado
  global matriz_1
  global matriz_2

  for linhas in range(0, len(y)):
    for colunas in range(0, len(y)):
      linha_temp.append(x * int(y[linhas][colunas]))
    resultado.append(linha_temp)
    linha_temp = []

  if matriz_resultado == "m2":
    matriz_2 = resultado
  elif matriz_resultado == "m1":
    matriz_1 = resultado
  

tamanho_das_2_matrizes = int(input())
matriz_1 = []
matriz_2 =[]
# Colocaremos os elementos da linha em uma lista 
# e depois adicionamos ela à matriz(lista):
for tamanho_1 in range(0, tamanho_das_2_matrizes):
  linha = input().split(" ")
  matriz_1.append(linha)
for tamanho_2 in range(0, tamanho_das_2_matrizes):
  linha_n = input().split(" ")
  matriz_2.append(linha_n)

quantidade_operacoes = int(input())
operacoes_restantes = quantidade_operacoes
for index in range(quantidade_operacoes):
  entrada = input().split(" = ")
  operacao = entrada[1]
  matriz_resultado = entrada[0]
  tipo_da_operacao(operacao)
  operacoes_restantes -= 1
  if tipo_operacao == "multiplicacao escalar":
    operacao_multiplicacao_escalar(inteiro_k, matriz_multiplicada)
  elif tipo_operacao == "multiplicacao":
    operacao_multiplicacao_matrizes(elemento_1, elemento_2)
  elif tipo_operacao == "soma":
    operacao_soma(elemento_1, elemento_2)
  elif tipo_operacao == "subtracao":
    operacao_subtracao(elemento_1, elemento_2)
  string_linha = str()
for linhas_resultado in range(0, len(resultado)):
  for colunas_resultado in range(0, len(resultado)-1):
    string_linha += str(resultado[linhas_resultado][colunas_resultado]) + " "
  string_linha += str(resultado[linhas_resultado][len(resultado)-1])
  print(string_linha)
  string_linha = str()

