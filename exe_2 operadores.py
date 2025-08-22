#controle de acesso

#variaves

lista='sim'
ingresso='sim'

digi_lista=input('voce esta na lista vip?:')
digi_ingresso=input('voce esta com o ingresso?:')

#condicoes

if digi_lista==lista or digi_ingresso== ingresso:
    print('entrada permitida!')
else:
    print('entrada negada!')