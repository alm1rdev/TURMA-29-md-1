#caractere especial

cri=input('crie um nome de usuario valido?').lower()

if  ('@' or '!'or '$'or'#') not in cri:# nao sei porque precisou do parrenteses para funcionar
  print('sue usuario e valido')

else:
  print('sue nome de usuario e invalido')