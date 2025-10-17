
# items()-traz chave e valor de um dicionario 
# values()-traz os valores de um dicionario
a,b=1,2
a,b=b,a
pessoa={
    'nome':'almir',
    'sobrenome':'silva'
}


complento_pessoa={
    'altura':'1.72',
    'idade':'19'
}


pessoa_completa={**pessoa,**complento_pessoa}


def dicionario(*args,**kwargs):
    for chave, valor in kwargs.items():
        print(chave,valor)


    return args

print()








# a,b= pessoa.values()
# print(a,b)
# for chave,valor in pessoa.items():
#     print(chave,valor)