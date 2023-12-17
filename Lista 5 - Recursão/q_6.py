import math

def bin(lista, menor, maior, destino, lista_direcoes):
 
    # Caso base
    if maior >= menor and int(lista[menor]) <= destino and int(lista[maior]) >= destino:
 
        meio = math.ceil((maior + menor) / 2)
 
        if int(lista[meio]) == destino or (len(lista[meio]) != destino and len(lista) == 1):
            lista_direcoes.append("Meio")
            return meio
 
        elif int(lista[meio]) > destino:
            lista_direcoes.append("Esquerda")
            return bin(lista, menor, meio - 1, destino, lista_direcoes)
 
        elif int(lista[meio]) < destino:
            lista_direcoes.append("Direita")
            return bin(lista, meio + 1, maior, destino, lista_direcoes)
 
    else:
        # Se elemento não estiver presente na lista
        lista_direcoes.append("Meio")
        return -1

# Entradas e declaração de variáveis:
numeros_entrada = input().split(" ")
dica = int(input())
bits_dave = int(input())
lista_direcoes = []
string_direcoes = str()

# Chamando a função recursiva:
bin(numeros_entrada, 0, len(numeros_entrada) - 1, dica, lista_direcoes)

# Construção da string que possui as direções que Dave deve seguir:
if len(lista_direcoes) > 1:
    for i in range(0, len(lista_direcoes) - 1):

        string_direcoes += lista_direcoes[i] + " -> "
    string_direcoes += lista_direcoes[-1]
else:
    string_direcoes = lista_direcoes[0]

# Cálculo número binário:
valor_novo = dica
valor_final = str()

if dica > int(numeros_entrada[-1]) or dica < int(numeros_entrada[0]):
    print("Acho que a Doutora se confundiu, pois é impossível chegar nesse número pois ele é menor que a menor sala ou maior que o maior da sala.")

else:
    while valor_novo != 0 and valor_novo // 2 >= 1 and (valor_novo % 2 == 1 or valor_novo % 2 == 0):
      resto = int(valor_novo % 2)
      valor_final = str(resto) + valor_final
      valor_novo = int(valor_novo//2)
    if dica == 0:
      valor_final = "0"
    else:
      valor_final = "1" + valor_final
    # valor_final = número binário convertido

    if len(valor_final) > bits_dave and str(dica) in numeros_entrada:
      print("Consegui encontar a saída, mas não consigo falar pois o número é muito grande para essa quantidade de bits.")
    
    elif str(dica) not in numeros_entrada and len(valor_final) <= bits_dave:
      print(f'{string_direcoes}, mas não consegui achar.')

    elif str(dica) not in numeros_entrada and len(valor_final) > bits_dave:
      print("Busquei muito, mas não achei a sala, que nem posso dizer, já que tenho poucos bits.")
    
    else:
      # Adicionando "zeros" para igualar à quantidade de bits que Dave possui:
      n = len(valor_final)
      while n != bits_dave:
        valor_final = "0" + valor_final
        n += 1

      print(f'{string_direcoes}, seguindo por essas coordenadas você vai chegar no número {valor_final}.')

