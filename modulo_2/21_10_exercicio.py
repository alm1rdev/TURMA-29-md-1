numeros=[1,2,3,4,5,6,7,8,9,10]


# tira=list(filter(lambda n:n % 2==0,numeros))

# def dobro(n):
#     return n*2

# dobra=list(map(dobro,tira))

# print(dobra)
#--------------------------------
#   list compreension (LC)
# pares=[n*2 for n in numeros]
# print(pares)

string=[str(n) for n in numeros]
# print(string)





#calcular imc 

imc=[(80,1.5),(110,1.9)]

resultado=[p/a**2 for p, a in imc]

# print(f'{resultado}')


#--------------------------------------
#       filter e map

pares= [n*2   for n in numeros if n % 2 ==0]
#     ( map 🔺)               (filter🔺)
# print(pares)


num=[-5,0,1,5,-10,-20,6]

positivos=[n for n in num if n >=0]
print(positivos)