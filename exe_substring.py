#encontrar palavra especifica

diggi_frase=input('diigite uma frase:').upper()
palavra_especifica=input('digite a palavra a ser encontrada na frase:').upper()

if palavra_especifica in diggi_frase:
    print("a palavra esta na frase")

else:print('a palavra nao esta na frase')