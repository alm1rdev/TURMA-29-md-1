#----------------------------------
#         revisao
#--------------------------------

#  o END  um parametro usado no print que cada vez que o print for esxecutado o end da um enter e p proximo print
# e exibido em outra 

#------------------------------------

#         FUNCAO TIME 

#-------------------------------------
# basicamente essa funcao usa uma biblioteca para trabalhar com o tempo ,suas utilidades vao de pausar o programa 
# por um determinado tempo em secundos ou ver e usar o horario atual

# import time
# for i in range(11,1,-1):
#     print(i-1,end='\n')
#     time.sleep(1)
# print('acabou')

#----------------------------------

#      funcao FILTER

#------------------------------------

# A função filter() serve para filtrar elementos de uma sequência (lista, tupla, etc.),;
#  mantendo apenas os que atendem a uma condição

#EXEMPLOS👇:

# def eh_par(numero):
#     return numero % 2 == 0

# numeros = [1, 2, 3, 4, 5, 6]
# pares = list(filter(eh_par, numeros))
# print(pares)

#usando a funcao lambda

# numeros=[1,2,3,4,5,6]
# pares=list(filter(lambda x:x %2==0,numeros))
# print(pares,end='\n')


#-➕exemplos
# exibi somente palavra scom menos de 4 letras

# palavras=['sol','ceu','terra','universo']

# def menos_4(palavras):
#     return len(palavras)<4

# resultado=list(filter(menos_4,palavras))
# print("-".join(resultado))

#-----------------------------------------------------------------
#filtra palvras com mais de 4 letras usando uma funcao lambda
#--------------------------------------------------------------------

# palavras = ["sol", "planeta", "lua", "estrela", "céu"]

# longas = list(filter(lambda p: len(p) > 4, palavras))
# print(longas)


#------------------------------------------

#       funcao sorted

#----------------------------------------------

# essa funcao coloca em ordem os items de um conjunto de dados do menor pra o maior ou ;
# ao contrario usando (reverse=True)

# exemplo=🔻

# salario=[100,3000,5000,18000]

# ordem=sorted(salario)
# print(ordem)

#do maior para o menor usando reverse=true

salario=[100,3000,5000,18000]

ordem=sorted(salario,reverse=True)
print(ordem)
