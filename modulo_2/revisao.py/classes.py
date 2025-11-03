import time
class carro:
    def __init__(self,marca,modelo,ano_fabricaçao,velocidade_maxima,hp):
        self.marca=marca
        self.modelo=modelo
        self.ano_fabricaçao=ano_fabricaçao
        self.velocidade_maxima=velocidade_maxima
        self.hp=hp
  
    def ligar(self):
            print('ligando o carro...')
            time.sleep(1)
            print('aquencendo o motor...')
            time.sleep(3)
            print('...pronto para sair ✔ 🚗')
        
    def conduzindo(self):
            time.sleep(2)
            print('dirigindo na estrada...')
            time.sleep(3)
            print('caiu em uma blitz 👮‍♂️🚓')
            time.sleep(3)
            print('o policial analisou o carro e constatou que era um',end='\n')
            print( self.marca,
                  self.modelo,
                  self.ano_fabricaçao,
                  self.velocidade_maxima,
                  self.hp)
            time.sleep(2)
            print('...foi liberado e seguiu seu rumo.')
informacoes=carro('Fiat','Strada','ano-2024','VM-180','hp-109')
informacoes.ligar()
informacoes.conduzindo()