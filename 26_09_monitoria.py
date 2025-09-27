notas=[]

contador=1
while True:
   if contador ==5:
     break
   notas_dig=float(input('digite sua nota:'))

   notas.append(notas_dig)
   contador+=1

   media=sum(notas)/4

   if media >=7:
      print(f'sua  edia foi {media:.1f} , aprovado')
      break

   else:
      print(f'sua media foi `{media:.1f} ,reprovado mas...')

      recuperacao=float(input('digite a nota  da recuperacao:'))

      resultado=(media+recuperacao)/2

      if resultado>=7:
         print(f'agora foi aprovado,sua nota foi {resultado:.1f}')
      else:
         print(f'que pena sua media foi {resultado:.1f} ,estude mais no proximo ano')