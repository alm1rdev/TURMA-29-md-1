#criar um alista semana 
#dentro da lista segunda , terca ,quarta,quinta,sexta
# o usuario vai poder inserir,apagar,listar
# e sair suas atividades diarias
import os
semana=[[],[],[],[],[]]

while True:

    o_q_fazer=input('o que deseja fazer:[i]inserir,[a]apagar,[l]listar>:').lower()
    try:  
       if o_q_fazer=='i':
    
         qual_dia=int(input(' dia da semana que agendar:0,1,2 ,3,4(segunda,terca, quarta, quinta,sexta):'))

         if qual_dia==0:
                segunda=input('digite seus compromissos:')
                semana[0].append(segunda)
        
         elif qual_dia==1:
                terca=input('digite seus compromissos:')
                semana[1].append(terca)
           
         elif qual_dia==2:
                quarta=input('digite seus compromissos:')
                semana[2].append(quarta)
           
         elif qual_dia==3:
                quinta=input("digite seus compromissos:")
                semana[3].append(quinta)
           
         elif qual_dia==4:
                sexta=input('digite seus compromissos:')
                semana[4].append(sexta)
    except ValueError:
          print('digite apenas numeros!')

    try:
            
            if o_q_fazer=='a':
                  
              apagar=int(input('qual dia quer mudar:'))

              if apagar==0:
                   print(semana[0])
                   
                   compromissso_0=int(input('qual o compromisso quer deletar:'))
                   
                   del semana[0][compromissso_0] 

              elif apagar==1:
                 print(f'seus compromissos do dia>:',{semana[1]})
                 compromisso_1=int(input('qual compromisso quer deletar:'))

                 del semana[1][compromisso_1]

              elif apagar==2:
                   print(semana[2])
                   compromisso_2=int(input('qual compromisso quer deletar:'))
                   del semana[2][compromisso_2]
            
              elif apagar== 3:
                   print(semana[3])

                   compromisso_3=int(input('qual compromisso quer apagar:'))
                   del semana[3][compromisso_3]
              elif apagar==4 :
                   print(semana[4])

                   compromisso_4=int(input('qual compromisso quer deletar:'))
                   del semana[4][compromisso_4]

                   

    except ValueError :
         print('digite apenas numeros')  
    except IndexError:
         print('nao tem nenhum compromisso')  
 
    if o_q_fazer =='l':
        
        for indice,compromissos in enumerate(semana,start=1):
                
                    ver_qual_dia= input('quer ver os compromissos de qual dia, ou digite sair para outras ' 
                    'escolhas:')
                    if ver_qual_dia=='sair':
                         break
                    else:
                         ver_qual_dia=int(ver_qual_dia)

                    compromissos=semana[ver_qual_dia]

                    if ver_qual_dia==0:
                        os.system('cls')
                        print('os comprmissos para esse dia sao:')
                        print(f'{indice} - {compromissos}')
                        

                    elif ver_qual_dia ==1:
                        os.system('cls')
                        print('os comprmissos para esse dia sao:')
                        print(f'{indice} - {compromissos}')
                        
                    elif ver_qual_dia==2:
                        os.system('cls')
                        print('os comprmissos para esse dia sao:')
                        print(f'{indice} - {compromissos}')
                        
                    elif ver_qual_dia==3:
                        os.system('cls')
                        print('os comprmissos para esse dia sao:')
                        print(f'{indice} - {compromissos}')
                        
                    elif ver_qual_dia==4:
                        os.system('cls')
                        print('os comprmissos para esse dia sao:')
                        print(f'{indice} - {compromissos}')
                        continue
                    else:
                        print ('digite somente numeros!')
                        




           

        
        

