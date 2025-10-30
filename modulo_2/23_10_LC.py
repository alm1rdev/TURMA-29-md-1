#-------------------------------

#        LC lista compreension


# lista=[n*2 for n in range(10)if n%2==0]


#for dentro de for 🔻

lista=[
    (n,m)
    for n in range(4)
    for m in range(4)

]
# print(lista)



produtos=[
    {'nome':'cafe','preco':10},
    {'nome':'agua','preco':5},
    {'nome':'acucar','preco':7.5}
]

# atualizar_produtos=[
#     # (chave,valor)
#     # for chave,valor in produto['preco'] for chave,valor in produto['preco']
    
# ]

atualizar_produtos=[
    {**produto,'preco':produto['preco']*1.05}
    if produto['preco'] >=7.5 else {**produto}     
     for produto in produtos

]
print(*atualizar_produtos,sep='\n')

saida=[
    f'nome:{produto['nome']}-valor:{produto['preco']:.2f}'
    for produto in atualizar_produtos
]
# print(*saida  ,sep='\n')

#------------------------------------------

#          lc com dicionario

dict={'produto':'caneta',
      'preco':1.5,
      'cor':'preta'}

dict_upper={
    chave:valor.upper()                #◀map
    if isinstance(valor,str)else valor #◀map
    for chave,valor in dict.items()
    if chave !='preco'#◀filter
    
}
print(dict_upper,sep='\n')