pc= 6
fileira=4

numero_fileira = 0
while numero_fileira<=fileira:
    numero_fileira+=1
    numero_pc=1
    while numero_pc<=pc:
        print(f'{numero_fileira=} {numero_pc=}')
        numero_pc+=1
else:
    print('terminou')