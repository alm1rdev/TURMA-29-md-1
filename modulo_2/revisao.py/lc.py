precos=[100,200,300,400,700]

com_imposto=[preco*2 for preco in precos if preco>=250]
# print(com_imposto)


quadrado=[i for i in range(1,31) if i%3==0]
# print(quadrado)

palavras=['gato','ca','cavalo','urso']
tres_letras=[i for i in palavras if len(i)>3]
# print(tres_letras)

lista=['gato','macaco','muriçoca',12456]

letra=[i for i in lista if str(i).startswith('12')]  #endswith('a')
print(letra)                # existe o 🔺e o            🔺 eles verificam se existem a
# str comeca ou termina usando algum carcteres em especifico,servem par numeros tambem mas tem que converter par str