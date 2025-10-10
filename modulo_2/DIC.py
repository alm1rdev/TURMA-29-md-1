# pessoa={
#  'nome':'almir',
#  'sobrenome':'silva',
#  'idade':18,
#  'altura':1.72,
#  'endereços':[
#      {'rua': 'mutuca','numero':0},
#      {}
#  ],

# }
# for chave in pessoa:
#     print(chave,pessoa[chave])



    #exercicio

perguntas=[
    {
        'pergunta':'quanto e 2 + 2?',
        'opcoes':['1','3','4'],
        'resposta':'4',
    },
    {
        'pergunta':'quanto e 5*5 ?',
        'opcoes': ['25','55', '10','51'],
        'resposta':'25',

    },
    {
        'pergunta':'quanto e 10/2?',
        'opcoes':['4','5','2','1'],
        'respostas':'5',

    },

    ]
qtd_acertos=0

for pergunta in perguntas:
    print('Pergunta: ',pergunta['pergunta'])
    print()

    opcoes=pergunta['opcoes']

    for i,opcao in enumerate(opcoes):
        print(f'{i})', opcao)
        print()

    escolha =input('escolha uma alternativa:  ')

    resposta=False

    escolha_int=None

    qtd_escolha=len(opcoes)
    

    if escolha.isdigit():
        escolha_int=int(escolha)
    if escolha_int is not None:
        if escolha_int>=0 and escolha_int<=qtd_escolha:
            if opcoes[escolha_int]==pergunta['resposta']:
                resposta=True

    if resposta:
        print('responda certa (☞ﾟヮﾟ)☞  ✔ ☜(ﾟヮﾟ☜')
        qtd_acertos+=1
    else:
        print('resposta errada ¯\_(ツ)_/¯')

print(f'voce acertou {qtd_acertos} de {len(perguntas)}')
