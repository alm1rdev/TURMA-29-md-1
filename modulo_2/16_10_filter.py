num=[1,2,3,4,5]

def pares(n):
    return n % 2==0
resultado=list(filter(pares,num))
print(resultado)




conta=list(filter(lambda n :n % 2 ==0 ,range(1,11)))
print(conta)