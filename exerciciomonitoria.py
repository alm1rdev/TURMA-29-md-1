import random

numero_aleatorio=random.randint(1,5)

print('adivinhe o numero de 1 a 20 se quiser sair digite sair')

contador=0

while True:
   
   numero=input('diga sue palpite')
#saida
   while contador <5:
      if numero.isdigit():
        palpite= int(numero)
      if palpite < numero_aleatorio:
          print('muito baixo')
          contador+=1
      elif palpite > numero_aleatorio:
            print ('muito alto')
            contador+=1
      elif palpite == numero_aleatorio :
               print('parabense acertou')
               contador+=1
               dinovo=input('deseja continuar:sim / nao')
               continue
      elif dinovo.lower() =='nao':
               print('jogo encerrado') 
               break
       
      else:
       print('nao e um numero')
       continue