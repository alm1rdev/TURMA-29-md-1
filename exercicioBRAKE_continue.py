#caçculadora  loop

while True:
    numero_1=(input('digite um numero ou digite sair para sair')).isdigit()
    operador= input('qual tipo de operacao:')
    numero_2=     (input('digite outro numero:'))

    if (numero_1  and numero_2).isdigit() and operador=='+':
        print(numero_1 + numero_2)
 elif (numero_1  and numero_2).isdigit() and operador =='-'
        print(numero_1-numero_2)
    elif operador=='/':
        print(numero_1/numero_2)
    elif operador=='*':
     print(numero_1*numero_2)
     continue

    elif(  numero_1 or numero_2 or operador).lower()=='sair':
       print('voce quis parar')
       break