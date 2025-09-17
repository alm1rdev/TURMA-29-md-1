
#lista de compras
try:
 lista=[]
 print('vamos fazer uma lista de compras')

 while True:

  

  inicio=input('digite [i] para inserir ,[a] para apágar,[l] para listar ou [s] para sair :').lower()

  if inicio!='s':
    
      if inicio =='i':
         inicio=input('o que deseja adicionar a lista :').lower()
         lista.append(inicio)
      elif inicio=='a':
        apg=input('o que deseja apagar: ').lower()
        del(lista[])
      elif inicio =='l':
        for indice,lista in enumerate (lista):
         print( indice,lista)



  else:
    print('lista de compras encerrada')
    break
except:
  print('erro')



