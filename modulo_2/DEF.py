# def soma(*args):
#     total=sum(args)
#     print('-'*12)
#     print(f'o resulado e {total}')
#     print('-'*12)
# soma(3,4,5,9)  


def contador(*args):
    tam=len(args)
    print(f'recebi os numeros {args} e  totalizando sao {tam} numeros')


contador(4,7,9,89)