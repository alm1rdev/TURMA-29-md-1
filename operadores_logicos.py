# operadores logicos ou operadores booleanos
# and | or | not
# e   | ou | não 

#variaveis
idade= 18
habilitacao_2= 'sim'
carro='sim'


# perguntas
tem_carro= input('voce tem carro?')
pergunta_1 = int(input('qual a sua idade?'))
pergunta2=input('voce tem cnh?')

#condicionando
if idade >=18 and pergunta2== habilitacao_2 and tem_carro==carro:
    print('pode dirigir')
else:
    print('nao pode dirigir')