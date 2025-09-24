



#calculo do primeiro digito do cpf 


#ex:


cpf='197.760.870-19'.replace('.','').replace('-','')

nove_digitos=cpf[:9]

contador1=10

somados_nove=0

for indice in  nove_digitos:
 
 somados_nove+=int(indice)* contador1

 contador1-=1

total_nove_digitos=(somados_nove*10)%11

digito1=total_nove_digitos if total_nove_digitos <=9 else 0

print(digito1)
   
   

   