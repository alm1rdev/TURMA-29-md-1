#variavel= ' pedro'
 #         0     1   2     3  4  5     6   7
#texto= ['turma',True,bool,10,20,float,[],'almir']

#texto2=[2,3]

#texto.append('aluno novo') sempre adicina  FINAL da lista

#texto.insert(5,'mais') adiciona em um LUGAR especifico

#texto.pop(3) # pop remove mas pod eser recuperado 

#del(texto[4])  ee

#texto.clear() # limpa toda a lista

#texto.extend(texto2) extende a lista

# +  concatena listas

#tipo lista = mutavel





lista1, *resto= ['natan','matheus','samuel','hudson','thais','antonio','larissa','maria fernanda','josivanio','carlos','rielson','regivan','almir']

print(lista1)
#nome.sort() deixa tudo em ordem alfabetica( serve tanto para numeros quantos para palavras(strings))



for i in range(len(lista)):
    print(f'{i+1}   {lista[i]}')