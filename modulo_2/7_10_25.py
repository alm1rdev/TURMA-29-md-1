#def dentro de def 

def saudacao(msg,nome):
    def saudar():
        return f'(msg),(nome)'
    return saudar

saudacao1=saudacao('boa noite')
saudacao2=saudacao('bom dia')
