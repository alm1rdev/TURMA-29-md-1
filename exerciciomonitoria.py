import random

numero_aleatorio=random.randint(1,21)

print('adivinhe o numero de 1 a 20 se quiser sair digite sair')


while True:
   
   numero=input('giga sue palpite')

   if numero.lower()=='sair':
    print(f'voce desistiu o numero era {numero_aleatorio}')
    break

   if numero.isdigit():
      palpite= int(numero)
      if palpite < numero_aleatorio:
         print('muito baixo')
      elif palpite > numero_aleatorio:
         print ('muito alto')
      else:
         print('parabense acertou')
         break
   else:
      print('nao e um numero')
      continue