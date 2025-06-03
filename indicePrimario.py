import os

class indicePrimario:
    # atributos, elementos da estrutura
    #1. (disco) arquivo de dados
    __arquivoDados = None
    #2 (ram) tabela de indices
    __arrayIndice = list() 
    #3 (disco) arquivo de indices (backup)
    __arquivoIndices = None
    #
    
    
    # metodos
    #5. construir/criar(arquivo = None)
    def __init__(self, arqDados, arqIndices):
        self.__arquivoDados = open(arqDados, 'r')
       
        if(os.path.isfile(arqIndices)):
            print("O arquivo de indice primario existe")
            
            with open(arqIndices, 'r') as f:
                for linhas in f:
                    chave, RRN = linhas.split()
                    self.__arrayIndice.append((chave, int(RRN)))
            
            print(self.__arrayIndice[:10])                
        else:
            print("Não existe o arquivo de indice primário")
            self.__arquivoIndices = open(arqIndices, 'w')
           
            registros = self.__arquivoDados.readlines()
            RRN = 0            
            for r in registros:
                chave = self.criaChaveCanonica(r)
                self.__arrayIndice.append((chave, RRN))
                RRN = RRN + 1
               
            for i in self.__arrayIndice:
                self.__arquivoIndices.write(f'{i[0]} {i[1]}\n')
    
    def criaChaveCanonica(self, r):
        campos = r.split("|")
        chave = campos[0].upper().replace(' ', '')
        return chave           
    
    # ---------------------------------
    # --------------------------------- 

    #4. destruir
    def __del__(self):
        pass
    #3. pesquisa(chave)
    # a chave é a chave canonica do registro que se deseja encontrar
    def pesquisar(self, chave):
        
        # pesquisar a chave na tabela de indices usando busca binaria
        # a. (achou) acessar o RRN correspondente da chave encontrada
        # retornar pro usuario (true, RRN)
        
        # b. (nao achou) retornar pro usuario(false, None)
        pass
    
    def buscaBinaria(self, chave):
        # Inicialização das variáveis
        self.__arrayIndice.sort()
        inicio = 0
        fim  = len(self.__arrayIndice) - 1

        # Laço principal
        while(inicio <= fim):
            meio = (inicio + fim)//2
            if(self.__arrayIndice[meio] == chave):
                # retorno se houve sucesso (achou o elemento)
                return (True, self.__arrayIndice[meio][1])
            elif (chave < self.__arrayIndice[meio]):
                fim = meio-1
            else:
                inicio = meio+1
        # retorno em condiçoes de falha
        return (False, None)
    
    #1. inserir(registro)
    def inserir(self, registro):
        pass
    #2. remover(chave)
    def remover(self, chave):
        pass
    #