# validacao de senha pela quantidade de caracteres

diggi_senha=input('digite uma senha de 8 carcteres:')
print(f'a senha digitada  tem {len(diggi_senha)} caracteres...')

if (len(diggi_senha))>=8:
    print('Sua senha é valida').upper()
else:
    print('sua senha nao tem o numero de caracteres necessarios')
