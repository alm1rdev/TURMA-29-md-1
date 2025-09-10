# tabuada

#variavel.isdigit() verifica se foi digitado um numero ex:


contador=0



numero=int(input("digite qual o numero da tabuada :") )
while contador<=10:
   tabuada= numero* contador
   print(f' {numero} x {contador} = {tabuada}')

   contador+=1
   if numero.isdigit():
    print('digite um numero')

   