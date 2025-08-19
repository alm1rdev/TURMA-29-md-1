# calculadora simples

n1=int(input("digite um numero :"))
operador=input('escolha um operador numerico [+  -  *  /] :')
n2=int(input ('digite mais um numero para a equacao :'))

if operador== '+':
   print(n1 + n2)

elif operador=='-':
  print(n1- n2)

elif operador=='*':
   print(n1*n2)

elif operador=='/':
      if n2== 0:
          print(f'{n1}')
      else:print( n1/n2)

else:print('erro,escolha um dos operadores indicados antigamente')