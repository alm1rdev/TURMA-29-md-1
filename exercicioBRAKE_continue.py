#caçculadora  loop

while True:
    numero_1=input('digite um numero ou digite sair para encerar : ')
    if numero_1.lower()=='sair':
        print('calculadora encerrada')
        break
    operador=input('digite tipo de operacao ou SAIR:')
    numero_2=input('digite outro numero SAIR : ')

    if operador .lower()=='sair':
        print('calculadora encerrada')
    elif numero_2.lower()=='sair':
        print('calculaora encerrada')
    if numero_1.isdigit() and numero_2.isdigit():
        numero_1= float(numero_1)
        numero_2= float(numero_2)

        if operador =='+':
            print(numero_1+numero_2)
        elif operador == '-':
            print(numero_1-numero_2)
        elif operador =='/':
            if numero_2!=0:
             print(numero_1 / numero_2 )
            else:
                print('erro ,digite um operador valido')
                continue
        elif operador=='*':
            print(numero_1* numero_2)
        else: 
            print('ERRO digite um operador valido')
            continue
    else:
        print('digite numeros validos')
        continue