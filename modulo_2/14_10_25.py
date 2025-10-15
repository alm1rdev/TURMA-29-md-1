
#resolucao exercicio que  verifica se tem algum numero repetido dentro de alguma slistas apos encontrar a primeirra 
# repeticao sera 
# imprimida o primerios numero que se repetiu se nao existir numero repetido sera imprimido -1

# lista_de_listas_de_inteiros = [
#     [1, 2, 3, 4, 5, 6, 7, 8, 9, 10], 
#     [9, 1, 8, 9, 9, 7, 2, 1, 6, 8],
#     [1, 3, 2, 2, 8, 6, 5, 9, 6, 7],
#     [3, 8, 2, 8, 6, 7, 7, 3, 1, 9],
#     [4, 8, 8, 8, 5, 1, 10, 3, 1, 7],
#     [1, 3, 7, 2, 2, 1, 5, 1, 9, 9],
#     [10, 2, 2, 1, 3, 5, 10, 5, 10, 1],
#     [1, 6, 1, 5, 1, 1, 1, 4, 7, 3],
#     [1, 3, 7, 1, 10, 5, 9, 2, 5, 7],
#     [4, 7, 6, 5, 2, 9, 2, 1, 2, 1],
#     [5, 3, 1, 8, 5, 7, 1, 8, 8, 7],
#     [10, 9, 8, 7, 6, 5, 4, 3, 2, 1],
# ]


# def numero_duplicado(lista_de_listas_de_inteiros):
    # numeros_checados=set()
    # numero_repetido=-1
    # for numero in lista_de_listas_de_inteiros:
    #     if numero in numeros_checados:
    #         numero_repetido=numero
    #         break
    #     numeros_checados.add(numero)
    # return numero_repetido
    
# for lista in lista_de_listas_de_inteiros:
#     print(lista, numero_duplicado(lista))

    #---------------------------------------------------------------------------

    #                   funcao lambda

    #-----------------------------------------------------------------------------
# exercicio que coloca o indices do eixo x em crescente e o eixo y em decrescente e soma os indices e deixa em crescenttes
#minha resolucao

pontos=[
    (3,5),
    (1,9),
    (7,2),
    (4,4),
    (5,8)
]

eixo_x=sorted(pontos)
print(eixo_x)



#resolucao do professor

pontos_x_crescente=sorted(pontos,key=lambda p : p[0])
print('eixo x em ordem crescente')
for ponto_x in pontos_x_crescente:
    print(ponto_x)

pontos_y_decrescente=sorted(pontos,key=lambda p : p[1])
print('eixo y em decrescente')
for ponto_y in pontos_y_decrescente:
    print(ponto_y)


soma=sorted(pontos,key=lambda p:p[0] + p[1])
print(' soma dos eixos')
for resultado in soma:
    x,y=soma
    soma=x+y
    print(f'{x}+{y}={soma}')








