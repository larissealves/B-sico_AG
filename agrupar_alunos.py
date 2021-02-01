from random import random

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
        
       
        for i in range(len(caracteristicas)):
            if random() < 0.5:
                self.cromossomo.append("0") 
            else:
                self.cromossomo.append("1")  
      
        
    #AVALIAR
    def avaliacao(self):
        quantidade_cromossomos_1 = 0        
        soma_espaco_disponivel = 0
       
         
        for g in range(len(caracteristicas_grupo)):
           
            for i in range(len(caracteristicas)):
                 
                if(self.cromossomo[i]=='1'):
                    quantidade_cromossomos_1 += 1
                    if  quantidade_cromossomos_1 > self. limite_integrante_grupo:
                        print('GRANDE')
                    else:
                        nota_por_aluno =  self.caracteristicas[i].count(caracteristicas_grupo[g])
                        self.nota_avaliacao += nota_por_aluno 
                    #self.alunos_no_grupo = self.limite_integrante_grupo - quantidade_cromossomos_1 #diminuir espacoes disponiveis no grupo
        #print('\n', self.cromossomo, '= ', self.nota_avaliacao, '\n')
                    
                
    def crossover(self, outro_individuo):
        print('\noutro', outro_individuo.cromossomo)
        print('\ncromo 1', self.cromossomo)
        corte = round(random()  * len(self.cromossomo))
        print('\nPonto de corte', corte)
       
        filho1 = outro_individuo.cromossomo[0:corte] + self.cromossomo[corte::]
        filho2 = self.cromossomo[0:corte] + outro_individuo.cromossomo[corte::]
        
        filhos = [Individuo(self.nome, self.caracteristicas, self.limite_integrante_grupo, self.grupo, self.geracao + 1),
                  Individuo(self.nome, self.caracteristicas, self.limite_integrante_grupo, self.grupo, self.geracao + 1)]
        filhos[0].cromossomo = filho1
        filhos[1].cromossomo = filho2
        print('\nFilho 1', filho1)
        print('\nFilho 2', filho2)
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
    
if __name__ == '__main__':
    #p1 = Produto("Iphone 6", 0.0000899, 2199.12)
    lista_produtos = []
    lista_produtos.append(Produto("Geladeira Dako", 'B'))
    lista_produtos.append(Produto("Iphone 6",'B'))
    lista_produtos.append(Produto("TV 55' ", 'd'))
    lista_produtos.append(Produto("TV 50' ", 'B, C, D, B, B'))
    lista_produtos.append(Produto("TV 42' ", 'B'))
    lista_produtos.append(Produto("Notebook Dell", 'B'))
    lista_produtos.append(Produto("Ventilador Panasonic", 'B'))
    lista_produtos.append(Produto("Microondas Electrolux", 'B'))
    lista_produtos.append(Produto("Microondas LG", 'B, B'))
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


individuo2 = Individuo(nome, caracteristicas, numero_integrantes_grupo, caracteristicas_grupo)
individuo2.avaliacao()   

grupo1 = Grupo(caracteristicas_grupo, numero_integrantes_grupo)

individuo1.crossover(individuo2)

individuo1.mutacao(0.05)
individuo2.mutacao(0.05)
        

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