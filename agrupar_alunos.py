from random import random
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
        self.grupo = grupo
        self.nota_avaliacao = 0
        self.geracao = geracao
        self.cromossomo = []
        
        #Gerar pop aleatoriamente
        for i in range(len(caracteristicas)):
            if random() < 0.5:
                self.cromossomo.append("0")
                
            else:
                self.cromossomo.append("1")  
        print('CROMOSSOMOS: ',self.cromossomo)
        
        
    #AVALIAR
    def avaliacao(self):
        qnt_caracteristicas_iguais = 0
        notaPopulação = 0
        soma_espaco_disponivel = 0
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
                if (self.cromossomo[i] == '1') and (self.caracteristicas[i].count(caracteristicas_grupo[g])>=1):
                    notaAluno = self.caracteristicas[i].count(caracteristicas_grupo[g])
                    self.nota_avaliacao = notaAluno
                    print("\ncromossomo compativeis : ", self.nome[i], self.nota_avaliacao)
                #se o  cromossomo tiver sido escolhido para esta população e tiver ao menos uma caracteristica
                #compativel com as do grupo ele vai receber uma nota
         
if __name__ == '__main__':
    #p1 = Produto("Iphone 6", 0.0000899, 2199.12)
    lista_produtos = []
    lista_produtos.append(Produto("Geladeira Dako", 'A'))
    lista_produtos.append(Produto("Iphone 6",'A'))
    lista_produtos.append(Produto("TV 55' ", 'A'))
    lista_produtos.append(Produto("TV 50' ", 'B, C, D, B, B'))
    lista_produtos.append(Produto("TV 42' ", 'B'))
    lista_produtos.append(Produto("Notebook Dell", 'B'))
    lista_produtos.append(Produto("Ventilador Panasonic", 'B'))
    lista_produtos.append(Produto("Microondas Electrolux", 'C'))
    lista_produtos.append(Produto("Microondas LG", 'C'))
    lista_produtos.append(Produto("Microondas Panasonic", 'C'))
    lista_produtos.append(Produto("Geladeira Brastemp", 'C'))
    lista_produtos.append(Produto("Geladeira Consul", 'D'))
    lista_produtos.append(Produto("Notebook Lenovo", 'D'))
    lista_produtos.append(Produto("Notebook Asus", 'D'))
      
    lista_grupos = []
    lista_grupos.append(Grupo('B', 4))
    #lista_grupos.append(Grupo('A', 3))
    #lista_grupos.append(Grupo('C', 3))

nome = []
caracteristicas = []
grupo = []
for produto in lista_produtos:
    caracteristicas.append(produto.caracteristica)
    nome.append(produto.nome)
    

caracteristicas_grupo = []
numero_integrantes_grupo = 4
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