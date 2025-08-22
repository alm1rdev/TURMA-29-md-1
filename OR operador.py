nome_usuario='almir'
email= 'almir@exemplo.com'
senha=12345


#per
usuario=input('digite seu usuario:')
deemail=input(' digite seu email:')
senha_rece=int(input('digite sua senah:'))


#condiçoes
if not senha_rece:
    print('nao digitou a senha')
elif(usuario==nome_usuario or deemail==email) and senha==senha_rece:
    print('digite sua senha!')
else:'digite seu usuario ou email corretamente'