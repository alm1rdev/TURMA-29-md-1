#

senha_correta='certo99'
contador=0

while True:

    senha=input('digite a senha:')
    
      
    if senha.lower()== senha_correta:
        print('senha correta')
        break
        
    elif senha != senha_correta:
        print('senha errada')
        contador +=1
        if contador ==3:
            print('excesso de tentativas')
            break
        else:
            continue
    else:
        print('senha correta')
        break
    
      
