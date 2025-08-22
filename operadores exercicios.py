#entrega de comida

#variaveis

valor_compra=50 # ou +
localizacao='centro'

#perguntas

total_compra=float(input('digite o valor da sua compra:'))
entrega=input('qual a localizacao da entrega:')

#condiçoes

if total_compra >= valor_compra and entrega== localizacao:
    print('seu pedido sera entregue em breve!')
else:
    print('desculpe,seu pedido nao cumpre os requisitos de entrega!')