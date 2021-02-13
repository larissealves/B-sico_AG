from random import random

melhores_solucoes = []

class Produto():
    def __init__(self, nome, caracteristica):
        self.nome = nome
        self.caracteristica = caracteristica
        
class Grupo():
    def __init__(self, caracteristicas_grupo, numero_integrantes_grupo):
        self.caracteristicas_grupo = caracteristicas_grupo
        self.numero_integrantes_grupo = numero_integrantes_grupo
        self.grupo = []
              
        
class Individuo():
    def __init__(self, nome, caracteristicas, limite_integrante_grupo, grupo, geracao=0): #,,
        self.caracteristicas = caracteristicas
        self.nome = nome
        #self.valores = valores
        self.limite_integrante_grupo = limite_integrante_grupo
        self.alunos_no_grupo = 0
        self.grupo = grupo
        self.nota_avaliacao = 0
        self.geracao = geracao
        self.cromossomo = []
        
        
        a = 0
        #print(limite_integrante_grupo)
        for i in range(len(caracteristicas)):
            if random() < 0.5:
                self.cromossomo.append("0")
            else:
                self.cromossomo.append("1")
        
            if self.cromossomo[i] == '1':
                a +=1
                    
            if a > self.limite_integrante_grupo:
                if self.cromossomo[i] == '1':
                    self.cromossomo[i] = '0'

                if a < self.limite_integrante_grupo:
                    if self.cromossomo[i] == '0':
                        self.cromossomo[i] = '1'
                    

            
        #print("\n", self.cromossomo)
                            
       
        
    '''
    cont = 1
    while cont == self.limite_integrante_grupo
            for i in range(len(caracteristicas)):
            if random() < 0.5:
                self.cromossomo.append("0") 
            else:
                self.cromossomo.append("1")  
        #print("\naaaa i:", self.limite_integrante_grupo, "\n")
    '''      
    #AVALIAR
    def avaliacao(self):
        
        quantidade_cromossomos_1 = 0        
        soma_espaco_disponivel = 0
        nota_por_aluno = 0
       
        for g in range(len(caracteristicas_grupo)):
            
            for i in range(len(caracteristicas)):
                 
                if(self.cromossomo[i]=='1'):
                    quantidade_cromossomos_1 += 1
                    if self.caracteristicas[i].count(caracteristicas_grupo[g])== 0:
                        #print("0 CARACTERISTICAS1")
                        nota_por_aluno = 0
                    if self.caracteristicas[i].count(caracteristicas_grupo[g])== 1:
                        #print("1 CARACTERISTICAS")
                        nota_por_aluno = 1 
                    if self.caracteristicas[i].count(caracteristicas_grupo[g])> 2:
                        #print("2 ou + CARACTERISTICAS1")
                        nota_por_aluno = 2
                        #nota_por_aluno =  self.caracteristicas[i].count(caracteristicas_grupo[g])
        
                    self.nota_avaliacao += nota_por_aluno 
                    #self.alunos_no_grupo = self.limite_integrante_grupo - quantidade_cromossomos_1 #diminuir espacoes disponiveis no grupo
       # print('\n', self.cromossomo, '= ', self.nota_avaliacao, '\n')
        
                  
          
    
    def ordena_cromossomo(self):
         self.populacao = sorted(self.populacao,
                                key = lambda populacao: populacao.nota_avaliacao,
                                reverse = True)
    
    
    def crossover(self, outro_individuo):
        #print('\noutro', outro_individuo.cromossomo)
        #print('\ncromo 1', self.cromossomo)
        corte = round(random()  * len(self.cromossomo))
        #print('\nPonto de corte', corte)
       
        filho1 = outro_individuo.cromossomo[0:corte] + self.cromossomo[corte::]
        filho2 = self.cromossomo[0:corte] + outro_individuo.cromossomo[corte::]
        
        filhos = [Individuo(self.nome, self.caracteristicas, self.limite_integrante_grupo, self.grupo, self.geracao + 1),
                  Individuo(self.nome, self.caracteristicas, self.limite_integrante_grupo, self.grupo, self.geracao + 1)]
        filhos[0].cromossomo = filho1
        filhos[1].cromossomo = filho2
        #print('\nFilho 1', filho1)
        #print('\nFilho 2', filho2)
        return filhos
                   
    def mutacao(self, taxa_mutacao):
        #("\nAntes %s " % self.cromossomo, '\n')
        for i in range(len(self.cromossomo)):
            if random() < taxa_mutacao:
                if self.cromossomo[i] == '1':
                    self.cromossomo[i] = '0'
                else:
                    self.cromossomo[i] = '1'
       # print("Depois %s " % self.cromossomo)
        return self
    
    def proximo_grupo(self):
        pass
       
    
class AlgoritmoGenetico():
    def __init__(self, tamanho_populacao):
        self.tamanho_populacao = tamanho_populacao
        self.populacao = []
        self.geracao = 0
        self.melhor_solucao = 0
        
    def inicializa_populacao(self, nome, caracteristicas, limite_integrante_grupo, caracteristicas_grupo):
        for i in range(self.tamanho_populacao):
            self.populacao.append(Individuo(nome, caracteristicas, limite_integrante_grupo, caracteristicas_grupo))
        self.melhor_solucao = self.populacao[0]
   
    
        
    def ordena_populacao(self):
        self.populacao = sorted(self.populacao,
                                key = lambda populacao: populacao.nota_avaliacao,
                                reverse = True)
        
    def melhor_individuo(self, individuo):
        if individuo.nota_avaliacao > self.melhor_solucao.nota_avaliacao:
            self.melhor_solucao = individuo
        
    def soma_avaliacoes(self):
        soma = 0
        for individuo in self.populacao:
           soma += individuo.nota_avaliacao
        return soma
        
    def seleciona_pai(self, soma_avaliacao):
        pai = -1
        valor_sorteado = random() * soma_avaliacao
        soma = 0
        i = 0
        while i < len(self.populacao) and soma < valor_sorteado:
            soma += self.populacao[i].nota_avaliacao
            pai += 1
            i += 1
        return pai
    
    def visualiza_geracao(self):
        melhor = self.populacao[0]
        '''
        print("G:%s -> Valor: %s Espaço: %s Cromossomo: %s" % (self.populacao[0].geracao,
                                                               melhor.nota_avaliacao,
                                                               melhor.nome,
                                                               melhor.cromossomo))
        '''
    def resolver(self, taxa_mutacao, numero_geracoes, nome, caracteristicas, limite_integrante_grupo, caracteristicas_grupo):
        self.inicializa_populacao(nome, caracteristicas, limite_integrante_grupo, caracteristicas_grupo)
        

        for individuo in self.populacao:
            individuo.avaliacao()
        
        self.ordena_populacao()
        
        self.visualiza_geracao()
        
        for geracao in range(numero_geracoes):
            soma_avaliacao = self.soma_avaliacoes()
            nova_populacao = []
            
            for individuos_gerados in range(0, self.tamanho_populacao, 2):
                pai1 = self.seleciona_pai(soma_avaliacao)
                pai2 = self.seleciona_pai(soma_avaliacao)
                
                filhos = self.populacao[pai1].crossover(self.populacao[pai2])
                
                nova_populacao.append(filhos[0].mutacao(taxa_mutacao))
                nova_populacao.append(filhos[1].mutacao(taxa_mutacao))
            
            self.populacao = list(nova_populacao)
            
            for individuo in self.populacao:
                individuo.avaliacao()
                
            
            self.ordena_populacao()
            
            self.visualiza_geracao()
            
            melhor = self.populacao[0]
            self.melhor_individuo(melhor)
            
        '''
        print("\nMelhor solução -> G: %s Valor: %s Espaço: %s Cromossomo: %s" %
              (self.melhor_solucao.geracao,
               self.melhor_solucao.nota_avaliacao,
               self.melhor_solucao.nome,
               self.melhor_solucao.cromossomo))
        '''
        return self.melhor_solucao.cromossomo
        
        
        
if __name__ == '__main__':
   
    lista_produtos = []
    lista_produtos.append(Produto("Geladeira Dako", 'B'))
    lista_produtos.append(Produto("Iphone 6",'B'))
    lista_produtos.append(Produto("TV 55' ", 'A'))
    lista_produtos.append(Produto("TV 50' ", 'B, C, D, B, B'))
    lista_produtos.append(Produto("TV 42' ", 'B'))
    lista_produtos.append(Produto("Notebook Dell", 'C'))
    lista_produtos.append(Produto("Ventilador Panasonic", 'A'))
    lista_produtos.append(Produto("Microondas Electrolux", 'A'))
    lista_produtos.append(Produto("Microondas LG", 'A, A'))
    lista_produtos.append(Produto("Microondas Panasonic", 'C'))
    lista_produtos.append(Produto("Geladeira Brastemp", 'C'))
    lista_produtos.append(Produto("Geladeira Consul", 'D'))
    lista_produtos.append(Produto("Notebook Lenovo", 'B'))
    lista_produtos.append(Produto("Notebook Asus", 'D'))
      
    lista_grupos = []
    lista_grupos.append(Grupo('B', 6))
    lista_grupos.append(Grupo('A', 3))
    lista_grupos.append(Grupo('C', 3))
    lista_grupos.append(Grupo('D', 2))



        


nome = []
caracteristicas = []
grupo = []
for produto in lista_produtos:
    caracteristicas.append(produto.caracteristica)
    nome.append(produto.nome)
    
   

caracteristicas_grupo = []
numero_integrantes_grupo = []
for grupo in lista_grupos:
    caracteristicas_grupo.append(grupo.caracteristicas_grupo)
    numero_integrantes_grupo.append(grupo.numero_integrantes_grupo)
    #print(grupo.numero_integrantes_grupo)
   


'''   
ag = AlgoritmoGenetico(tamanho_populacao)
ag.inicializa_populacao(nome, caracteristicas, numero_integrantes_grupo, caracteristicas_grupo)
for individuo in ag.populacao:
    individuo.avaliacao()
    ag.ordena_populacao()
    ag.melhor_individuo(ag.populacao[0])
for i in range(ag.tamanho_populacao):
    print("*** Indivíduo %s ****\n" % i, 
          "Nome = %s\n" % str(ag.populacao[i].nome),
          "Caracteristicas = %s\n" % str(ag.populacao[i].caracteristicas),
          "Cromossomo = %s\n" % str(ag.populacao[i].cromossomo), '\n')
print("Melhor solução para o problema: %s" % ag.melhor_solucao.cromossomo,
          "Nota = %s\n" % ag.melhor_solucao.nota_avaliacao)
        
soma = ag.soma_avaliacoes()
#print("Soma das avaliações: %s" % soma)
        
nova_populacao = []
'''   
'''
for individuos_gerados in range(0, ag.tamanho_populacao, 2):
    pai1 = ag.seleciona_pai(soma)
    pai2 = ag.seleciona_pai(soma)
        
    filhos = ag.populacao[pai1].crossover(ag.populacao[pai2])
    nova_populacao.append(filhos[0].mutacao(taxa_mutacao))
    nova_populacao.append(filhos[1].mutacao(taxa_mutacao))
      
ag.populacao = list(nova_populacao)
for individuo in ag.populacao:
    individuo.avaliacao()
ag.ordena_populacao()
ag.melhor_individuo(ag.populacao[0])        
soma = ag.soma_avaliacoes()
print("Melhor: %s" % ag.melhor_solucao.cromossomo, "Valor: %s\n" % ag.melhor_solucao.nota_avaliacao)
''' 
cont = 0     
tamanho_populacao = 1
taxa_mutacao = 0.01
numero_geracoes = 1

numero_integrante = 0

for i in range(len(caracteristicas_grupo)):
        
    ag = AlgoritmoGenetico(tamanho_populacao)
    resultado = ag.resolver(taxa_mutacao, numero_geracoes, nome, caracteristicas, numero_integrantes_grupo[i], caracteristicas_grupo[i])
    print('*'*70)
    print('\n       GRUPO: ', caracteristicas_grupo[i], "->", " QNT Integrantes:", numero_integrantes_grupo[i], "       ")
    print('-'*70)
    for i in range(len(lista_produtos)):
        if resultado[i] == '1':
            melhores_solucoes.append(lista_produtos[i].nome)
            print('\n \n', lista_produtos[i].nome, ' = ', lista_produtos[i].caracteristica)
            print('\n')
   
                         
                
        

'''    


      
individuo1 = Individuo(nome, caracteristicas, numero_integrantes_grupo, caracteristicas_grupo)
individuo1.avaliacao()   


individuo2 = Individuo(nome, caracteristicas, numero_integrantes_grupo, caracteristicas_grupo)
individuo2.avaliacao()   

grupo1 = Grupo(caracteristicas_grupo, numero_integrantes_grupo)

individuo1.crossover(individuo2)

individuo1.mutacao(0.05)
individuo2.mutacao(0.05)


print('-------------------------')
n = 10
k = 3
print([(n // k) + (1 if i < (n % k) else 0) for i in range(k)])


if (self.cromossomo[i] == '1') and (self.caracteristicas[i].count(caracteristicas_grupo[g])>=1):
                    notaAluno = self.caracteristicas[i].count(caracteristicas_grupo[g])
                    self.nota_avaliacao = notaAluno
                    print("\ncromossomo compativeis : ", self.nome[i], self.nota_avaliacao)
                #se o  cromossomo tiver sido escolhido para esta população e tiver ao menos uma caracteristica
                #compativel com as do grupo ele vai receber uma nota
'''

#print('\n', melhores_solucoes)

