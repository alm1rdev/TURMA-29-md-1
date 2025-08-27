digi_palavra=input('digite uma palavra :').lower()

inverso=digi_palavra[-1::-1] # ou [::-1]

if inverso== digi_palavra :
    print(f'{inverso}  é um palindromo')
else:
    print('a palavra digitada nao é um palindromo')