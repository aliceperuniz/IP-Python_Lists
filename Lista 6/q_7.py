def pegar_chave(valor, qndt_cada_prato):
  for chave, value in qndt_cada_prato.items():
    if valor == value:
      return chave

# Dicionário que armazena ingredientes/pedidos com seus respectivos preços
preco_ingredientes = {"trigo": 3, "fermento": 2, "manteiga": 6, "ovos": 2, "batata": 4, "arroz": 3, "siri": 8, "pao": 2, "tomate": 2, "alface": 1, "picles": 3, "queijo": 5, "hamburguer de siri": 24, "pizza de siri": 42, "siri frito": 15, "siri a parmegiana": 24}
quantidade_ingredientes = {"trigo": 5, "fermento": 5, "manteiga": 5, "ovos": 5, "batata": 5, "arroz": 5, "siri": 5, "pao": 5, "tomate": 5, "alface": 5, "picles": 5, "queijo": 5, "hamburguer de siri": 5, "pizza de siri": 5, "siri frito": 5, "siri a parmegiana": 5}

# Quantidade que cada prato foi pedido ao longo do dia:
qndt_cada_prato = {"hamburguer de siri": 0, "pizza de siri": 0, "siri frito": 0, "siri a parmegiana": 0}

n = 0
itens_fora_do_cardapio = {}
dicionario_temp = {}
receitas_novas = {}
seguir = True

# Saldo inicial caixa:
saldo_caixa = 40

# Verificando se há entrada (já que o número de pedidos é indeterminado):
while n == 0:
  
  try:
    seguir = True
    pedido = input()
    if pedido == "hamburguer de siri" or pedido == "siri frito" or pedido == "pizza de siri" or pedido == "siri a parmegiana":
      print(f'{pedido} saindo...')
    else:
      pass
    if pedido == "hamburguer de siri":
      tupla = ("siri", "pao", "alface", "tomate", "queijo", "picles")
      qndt_cada_prato["hamburguer de siri"] += 1
    elif pedido == "siri frito":
      tupla = ("siri", "manteiga")
      qndt_cada_prato["siri frito"] += 1
    elif pedido == "pizza de siri":
      tupla = ("siri", "trigo", "fermento", "ovos", "queijo")
      qndt_cada_prato["pizza de siri"] += 1
    elif pedido == "siri a parmegiana":
      tupla = ("siri", "trigo", "ovos", "queijo", "tomate")
      qndt_cada_prato["siri a parmegiana"] += 1
    
    # Se for requisitado um pedido que não está no cardápio:
    else:
      if pedido not in itens_fora_do_cardapio:
        itens_fora_do_cardapio[pedido] = 1
        print(f'{pedido} ainda não é uma opção disponível.')
        seguir = False
      else:
        if itens_fora_do_cardapio[pedido] == 1:
          itens_fora_do_cardapio[pedido] = 2
          print(f'{pedido} ainda não é uma opção disponível.')
          seguir = False
        
        # Quando for requisitado mais de 2 vezes -> nova entrada com ingredientes para fazer uma receita nova:
        elif itens_fora_do_cardapio[pedido] == 2:
          itens_fora_do_cardapio[pedido] = 3
          qndt_cada_prato[pedido] = 0
          nova_receita = input().split(" ")
          tupla = tuple(nova_receita)
          receitas_novas[pedido] = tupla
          
          # Atribuindo um preço para o prato criado:
          preco = 0
          for item in range(0, len(tupla)):
            preco += preco_ingredientes[tupla[item]]
          preco += 5
          preco_ingredientes[pedido] = preco
          print(f'Atendendo demandas, {pedido} é a mais nova adição ao cardápio do Siri Cascudo.')
          seguir = False

        elif itens_fora_do_cardapio[pedido] > 2:
          qndt_cada_prato[pedido] += 1
          tupla = receitas_novas[pedido]
          print(f'{pedido} saindo...')
    
    if seguir == True: # Se for um pedido válido
      
      # Verificando se há ingredientes suficientes:
      for i in range(0, len(tupla)):

        # Se não tiver quantidade suficiente desse ingrediente:
        if quantidade_ingredientes[tupla[i]] <= 0:
          # Comprando o ingrediente que falta (4 unidades por vez):
          saldo_caixa -= 4*(preco_ingredientes[tupla[i]])
          quantidade_ingredientes[tupla[i]] += 4
          quantidade_ingredientes[tupla[i]] -= 1
        # Se houver ingredientes suficientes:
        else:
          quantidade_ingredientes[tupla[i]] -= 1

      # Recebendo o valor do prato vendido:
      saldo_caixa += preco_ingredientes[pedido]
          
    else: # Se não for um pedido válido
      pass

  except EOFError:
    n = 1

print("##### Fim do expediente #####")
print(f'O lucro obtido no dia de hoje foi de R${int(saldo_caixa - 40)}.')
  
# Vendo qual foi o prato mais vendido:
maior_valor = 0
for n in qndt_cada_prato.values():
  if n > maior_valor:
    maior_valor = n

# Vendo qual o prato(Chave) que corresponde ao maior valor:
mais_vendido = pegar_chave(maior_valor, qndt_cada_prato)
if mais_vendido == "hamburguer de siri":
  print("O bom e tradicional hambúrguer de siri, líder em vendas, nunca será superado!")
else:
  mais_vendido = mais_vendido.capitalize()
  print(f'{mais_vendido} está fazendo sucesso entre os clientes, ultrapassando até mesmo o lendário hambúrguer de siri.')
