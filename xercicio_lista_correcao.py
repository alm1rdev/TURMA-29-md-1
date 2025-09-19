print('vamos fazer sua lista de compras')

lista=[]
while True:
    entrada=input('[i]=inserir,[a]=apagar,[l]=listar,[s]sair')

    if entrada=='i':
       inserir=input('o que deseja aducionar:')
       lista.append(inserir)

    elif entrada=='a':
        apagar_str=input('DIGITE O NUMERO do item :')
        try:
            apagar_int=int(apagar_str)
            del lista[apagar_int]
        
        except ValueError:
            print('digite um numero inteiro')
        except IndexError:
            print('nao existe item com esse numero')
    elif entrada=='l':
        if len(lista)==0:
            print('a lista esta vazia')
        for indice ,nome in  enumerate(lista):
            print(indice+1, nome)
     
    elif entrada=='s':
        print('lista de compra s finalizada')
        break
    else:
        print('entrada invalida tente novamente')