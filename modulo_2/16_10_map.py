

# def quadrado(funcao,lista):
#     novalista=[]
#     for item in lista:
#         novalista.append(funcao(item))
#     return novalista

# def dobrar (n):
#     return n *2

# print(quadrado(dobrar([1,2,3,4,5])))

#----------------------------------------

#             MAP

num=[1,2,3,4,5
]
def dobrar(n):
    return n* 2

resultado= map(dobrar,num)
print(list(resultado))