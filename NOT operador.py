nome='almir'
senha='12345'


nome_digitado=input('digite seu nome:')
senah_digitada=input('digite a senha:')

if not senha:
    print(' voce nao digitou a senha')
elif nome_digitado==nome and senah_digitada== senha:
   print('acesso liberado')
else:
    print('acesso negado')