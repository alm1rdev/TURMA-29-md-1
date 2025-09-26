


import random

cpf_usuario=random.randint(0,9)

contador=9

novo_cpf=''

while contador:
   
   for digito in str(random.randint(0,9)):
 
    novo_cpf+= digito

    contador-=1

print( novo_cpf)

