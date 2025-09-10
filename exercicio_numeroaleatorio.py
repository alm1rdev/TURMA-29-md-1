import random

while True:
     numerosecreto= random.randint(1,10)

     tentativas = 0 
     quantidade_tentativas=5

     print('vamos jogar')

     while tentativas <= quantidade_tentativas:
           palpite=input('diga seu palpite:')

           if palpite.isdigit():
                 palpite=int(palpite)

                 tentativas+=1

                 if tentativas== quantidade_tentativas:
                       print(f'tentativas esgotadas, o numero era {numerosecreto}')
                       break
                 if palpite < numerosecreto:
                       print('palpite baixo,tente novamente')
                    
                 elif palpite>numerosecreto:
                       print('palpite alto,tente novamente')
                    
                 else:
                       print('parabens acertou')
                       break
           else:
             print('nao e um numero')
           continue
     continuar=input("deseja continuar jogando:sim ou nao:")

     if continuar.lower()!='sim':
                 print('obrigado por jogar')
                 break