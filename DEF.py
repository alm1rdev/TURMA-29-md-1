

# def Print():
#     print('almir')

#     Print()


   # -------------------------------------
# def nome(nome):
#     print(f'ola,{nome}')

# nome('almir')

#----------------------------

# def name(nome,idade=None):
    

#     if idade is not None:
#         print(f'ola,sou {nome} e tenho {idade}')
    
#     else:
#         print(f'ola, sou {nome}')

#     nome('almir',33)


    #---------------------------------------
num=(10,20,30,40)

total=1
def name(*args):
    total =0
    for numero in args:
        total+=numero
    return total

resultado= name(10,20,30,40)
print(resultado)


#--------------------------------

# def soma (x,y,z=None):#
#     total= x *y
#     divisao= x /y
    

#     return total

#     print(soma(2,3))


     
