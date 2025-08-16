# APROVADO OU REPROVADO

nota_1= int(input("digite nota 1 :"))
nota_2=int(input("digite nota 2 :"))
nota_3=int(input("digite nota 3 :"))
nota_4=int(input('digite nota 4 :'))
 
media=(nota_1+nota_2+nota_3+nota_4)/4
print( f'sua media é {media}')

if media >=7 :
 print("PARABENS, voce esta aprovado")

elif media >=5:
 print("que pena ,voce esta em recuperacao")

else:
 print('REPROVADO')