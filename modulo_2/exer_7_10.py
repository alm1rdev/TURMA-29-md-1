def produto(num):
resultado=produto(7)

print(resultado)
#-------------------------------------------------------------------------------
#                          resolucao
#----------------------------------------------------------------------------
def criar_multiplicar(multiplicador):
    def multipllicar(numero):
        return numero * multiplicador
    return multipllicar

dupli=criar_multiplicar(2)
tri=criar_multiplicar(3)
qua=criar_multiplicar(4)

print(dupli(3))
print(tri(3))
print(qua(4))
 


