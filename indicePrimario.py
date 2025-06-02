import os

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
    def __init__(self, arquivoDados = None, arquivoIndex = None):
        if arquivoDados == None:
            raise ValueError('Sem arquivo de dados. ')
        
        with open (arquivoDados, mode = 'r+', encoding='utf-8') as f:
            registros  = f.readlines()
        registros.pop(0)
        
        self.__arquivoDados = registros
        
        if arquivoIndex == None:
            print('Não existe arquivo Index. Criarei um.')
            for i  in range(len(registros)):
                aux = registros[i]
                
                stringList = aux.split(',')
                
				chave = stringList[0]
				chave = chave.replace(" ", "")
				chave = chave.upper()
            
            
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