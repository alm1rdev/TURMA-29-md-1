
try:
    num1=8
    num2=0
   
    num1 /num2

except Exception:
    print('erro')
#se nao ocorrer nenhum erro o programa vai direto para o else 
#so usa els ecom except
else:
    print('sem erro')

finally:
    print('executar sempre')
