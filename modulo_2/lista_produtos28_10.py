import copy
from exercicio28_10 import produtos

print(*produtos,sep='\n')
copia=copy.deepcopy(produtos)


#aumentando 10%  os precos do dict produtos
novos_produtos=[
    {**p,'preco':round(copia['preco']*1.1,2)}
    for p in copy.deepcopy(produtos)

]

print()
print(*novos_produtos,sep='\n')

produtos_por_nome=[
    sorted(
        copy.deepcopy(novos_produtos),
        key=lambda p:p['nome'],
        reverse=True
    )
]
print()
print(*produtos_por_nome,sep='\n')



