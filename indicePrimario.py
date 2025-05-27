

class indicePrimario:
    # atributos, elementos da estrutura
    #1. (disco) arquivo de dados
    __arquivoDados = None
    #2 (ram) tabela de indices
    __tabelaIndices = list() 
    #3 (disco) arquivo de indices (backup)
    __arquivoIndices = None
    #
    
    
    # metodos
    #5. construir/criar(arquivo = None)
    def __init__(self, arquivo = None):
        pass
    #4. destruir
    def __del__(self):
        pass
    #3. pesquisa(chave)
    def pesquisar(self, chave):
        pass
    #1. inserir(registro)
    def inserir(self, registro):
        pass
    #2. remover(chave)
    def remover(self, chave):
        pass
    #