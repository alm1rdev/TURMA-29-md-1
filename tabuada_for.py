while True:

        numero=int(input('digite o numero da  tabuada :'))


        for i in range(1,11):
            tabuada= i * numero
            print(f'{i} * {numero} = {tabuada}')
    
        dinovo=input('quer outra tabuada: sim ou nao :').lower()
        if dinovo =='sim':
            print('saindo outra tabuada ....')
            continue
        elif dinovo == 'nao':
            print('ok...tabuada encerrada')
            break
        else:
         print('digite sim ou nao')
         continue