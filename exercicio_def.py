numeros=[10,10,10,10,10,10,10,10,10,10]

def soma (numeros):
    total=sum(numeros)

def impar_par(num):
    resultado= num %2 
    if resultado == 0:
        return f'o{num}e par'
    return f'o {num}e impar'

print(impar_par(5))
print(impar_par(7))