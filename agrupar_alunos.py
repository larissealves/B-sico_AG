import random

individuos = 20
cromosomas = 6
generaciones = 3

class Produto():
    def __init__(self, nome, caracteristica):
        self.nome = nome
        self.caracteristica = caracteristica
        
class Grupo():
    def __init__(self, caracteristicas_grupo, numero_integrantes_grupo):
        self.caracteristicas_grupo = caracteristicas_grupo
        self.numero_integrantes_grupo = numero_integrantes_grupo
              
        
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
        
       
        #Gerar pop aleatoriamente
        #for i in range(len(caracteristicas)):
          #  if random() < 0.5:
         #       self.cromossomo.append("0") 
          #  else:
        #        self.cromossomo.append("1")  
       # print('CROMOSSOMOS: ',self.cromossomo)
      
        # a variavel "a" é a quntidade de individuos 
      
        a = len(caracteristicas)
        
        poblacion = [[0 for x in range(cromosomas)] for x in range(a)]
      
        
        for ind in range(a):
            for cromosoma in range(cromosomas):
               poblacion[ind][cromosoma] = random.randint(0, 1)
      
        #Imprime población
            
        print("\nPopulação Inicial\n")
        for individuo in range(a):
            print(str(individuo) + " - [" + ", ".join(str(f) for f in poblacion[individuo]) + "]")

        
    #AVALIAR
    def avaliacao(self):
        #notaPopulacao = 0
        soma_espaco_disponivel = 0
        a = 0
        for g in range(len(caracteristicas_grupo)):
            for i in range(len(self.cromossomo)):
                notaAluno = 0  
                
                ''' os cromossomos = 1
                desses quais realmente tem as caracteristicas definidas progrupo??
                verifico e dou uma nota com base nisso. 
                
                " aqui vai só pegar a população e dá uma nota com base na info acima"
                
                e fico com a melhor combinação (funçãoi selecionar) proxima fase
                
                se em 3 tentativas ele n chegar numa solução eu paro
                '''
                if (self.cromossomo[i] == '1'):
                    a += 1
                    if a> self. limite_integrante_grupo:
                        notaPopulacao = 1
                        print('MUITOS INTEGRANTES - PESSIMA POP')
                    else:
                        # a é a quantidade de cromossomos = 1
                        # verifico destes quais tem caracteristicas igual as requisitadas no grupo
                        # conto essa caracteristicas por alunos e somo todas
                        # 
                        if self.alunos_no_grupo < self.limite_integrante_grupo:
                            nota_por_aluno = self.caracteristicas[i].count(caracteristicas_grupo[g])
                            print('\nNOTA ALUNO: ', nota_por_aluno, '\n' )
                            self.nota_avaliacao += nota_por_aluno
                        self.alunos_no_grupo = self.limite_integrante_grupo - a
            
            print('\nESPAÇO LIVRE: ', self.alunos_no_grupo )
            print('\nTOTAL NOTA POPULAÇÃO:', self.nota_avaliacao)
                        
        ''' gero varias pop,
        
        
        '''
                
         
if __name__ == '__main__':
    #p1 = Produto("Iphone 6", 0.0000899, 2199.12)
    lista_produtos = []
    lista_produtos.append(Produto("Geladeira Dako", 'B'))
    lista_produtos.append(Produto("Iphone 6",'B'))
    lista_produtos.append(Produto("TV 55' ", 'B'))
    lista_produtos.append(Produto("TV 50' ", 'B, C, D, B, B'))
    lista_produtos.append(Produto("TV 42' ", 'B'))
    lista_produtos.append(Produto("Notebook Dell", 'B'))
    lista_produtos.append(Produto("Ventilador Panasonic", 'B'))
    lista_produtos.append(Produto("Microondas Electrolux", 'B'))
    lista_produtos.append(Produto("Microondas LG", 'B'))
    lista_produtos.append(Produto("Microondas Panasonic", 'B'))
    lista_produtos.append(Produto("Geladeira Brastemp", 'B'))
    lista_produtos.append(Produto("Geladeira Consul", 'B'))
    lista_produtos.append(Produto("Notebook Lenovo", 'B'))
    lista_produtos.append(Produto("Notebook Asus", 'B'))
      
    lista_grupos = []
    lista_grupos.append(Grupo('B', 6))
    #lista_grupos.append(Grupo('A', 3))
    #lista_grupos.append(Grupo('C', 3))

nome = []
caracteristicas = []
grupo = []
for produto in lista_produtos:
    caracteristicas.append(produto.caracteristica)
    nome.append(produto.nome)
    

caracteristicas_grupo = []
numero_integrantes_grupo = 6
for grupo in lista_grupos:
    caracteristicas_grupo.append(grupo.caracteristicas_grupo)
   
    
    
    
individuo1 = Individuo(nome, caracteristicas, numero_integrantes_grupo, caracteristicas_grupo)

individuo1.avaliacao()   
grupo1 = Grupo(caracteristicas_grupo, numero_integrantes_grupo)

print('\nGRUPO MOMENTO:',caracteristicas_grupo)
        
'''
print('-------------------------')
n = 10
k = 3
print([(n // k) + (1 if i < (n % k) else 0) for i in range(k)])'''

'''
               
if (self.cromossomo[i] == '1') and (self.caracteristicas[i].count(caracteristicas_grupo[g])>=1):
                    notaAluno = self.caracteristicas[i].count(caracteristicas_grupo[g])
                    self.nota_avaliacao = notaAluno
                    print("\ncromossomo compativeis : ", self.nome[i], self.nota_avaliacao)
                #se o  cromossomo tiver sido escolhido para esta população e tiver ao menos uma caracteristica
                #compativel com as do grupo ele vai receber uma nota
'''