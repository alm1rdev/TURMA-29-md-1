while True:

    n1=input('digite um nummero ou digite SAIR para encerar:')
    
    
    if n1.lower()=="sair":
       print('comparacao encerrada') 
       break
    n2=input('digite outro numero:')
    if not n1.isdigit() and n2.isdigit():
      print(' digite apenas numeros!')
      continue
    if n1 > n2:
        print(f'o {n2} e menor que {n1}.')
    elif n2> n1:

        print(f'o {n1} e menor que {n2}')
        continue

