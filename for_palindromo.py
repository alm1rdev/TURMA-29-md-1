palavra= input('digite uma palavra:').lower()

inverso= ''

for letra in range(len(palavra)-1,-1,-1):
    inverso+= letra

    if palavra == inverso:
        print(f'{palavra} e um paliindromo')
    else:
        print(f'{palavra} nao  e um paliindromo')