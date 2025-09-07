import random





while True:
   numero_aleatorio=random.randint(1,20)

 

   contador=0
   
  
   while contador !=5:
      print('adivinhe o numero de 1 a 20 se quiser sair digite sair')

      numero=input ("diga sue palpite ou digite 'sair' par encerrar:")
      if numero.lower()=='sair':
        print('jogo encerrado ')
        break
      if numero.isdigit():
          numero=int(numero)

          if numero < numero_aleatorio:
            print('muito baixo')
            contador+=1
          elif numero > numero_aleatorio:
            print ('muito alto')
            contador+=1
          elif numero== numero_aleatorio :
               print('parabense acertou')
               contador+=1
      else:
         print('digite apenas numeros!')  
         continue       
   if contador== 5 and numero !=numero_aleatorio:
      dinovo=input('suas tentativas acabaram ,deseja continuar :SIM/NAO : ')
      if dinovo.lower()=='sim':
          print('comecando um novo jogo...')
          continue
      elif dinovo.lower()=='nao':
          print('jogo encerrado,obrigado por jogar')
          break
       
       
   
